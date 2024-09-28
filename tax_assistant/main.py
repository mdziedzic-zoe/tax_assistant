import logging
import os
import uuid
from typing import List

import instructor
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.params import File
from openai import OpenAI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from tax_assistant.documents import process_document
from tax_assistant.models.partial_taxform import PartialDeklaracja

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = instructor.from_openai(OpenAI())
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: str
    content: str


class Request(BaseModel):
    conv_id: str
    messages: List[Message]
    declaration: PartialDeklaracja


class Response(BaseModel):
    response: str
    declaration: PartialDeklaracja


def get_system_prompt(current_state):
    return r"""
        You are an AI assistant specialized in Polish tax forms, particularly the PCC-3 form for civil law transactions tax. Your primary function is to interpret user input and extract relevant information to fill out the PCC-3 form accurately. Respond only in Polish.
        
        Key Guidelines:
        1. Extract only explicitly mentioned information from the user's input.
        2. Never assume or deduce information not directly stated.
        3. Ensure all extracted data adheres to the validation rules of the PCC-3 form.
        4. Highlight any validation issues in your response.
        5. Provide clear, concise responses focused on the user's most recent query.
        6. Consider the entire conversation history when extracting information.
        
        Data Model:
    
        class CelZlozenia(Enum):
            ZLOZENIE = 1
            KOREKTA = 2
    
        class PodmiotSkladajacy(Enum):
            PODMIOT_ZOBOWIAZANY = 1
            STRONA_UMOWY_ZAMIANY = 2
            WSPOLNIK_SPOLKI_CYWILNEJ = 3
            POZYCZKOBIORCA = 4
            INNY_PODMIOT = 5
    
        class PrzedmiotOpodatkowania(Enum):
            UMOWA = 1
            ZMIANA_UMOWY = 2
            ORZECZENIE_SADU_LUB_UGODA = 3
            INNE = 4
    
        class MiejscePolozenia(Enum):
            TERYTORIUM_RP = 1
            POZA_TERYTORIUM_RP = 2
    
        class TypSpolki(Enum):
            OSOBOWA = 1
            KAPITALOWA = 2
    
        class PodstawaOpodatkowania(Enum):
            ZAWARCIE_UMOWY_SPOLKI = 1
            ZWIEKSZENIE_MAJATKU_SPOLKI = 2
            DOPLATA = 3
            POZYCZKA_UDZIELONA_SPOLCE = 4
            ODDANIE_RZECZY_DO_UZYWANIA = 5
            PRZEKSZTALCENIE_SPOLEK = 6
            LACZENIE_SPOLEK = 7
            PRZENIESIENIE_SIEDZIBY = 8
    
    
        class SectionA(BaseModel):
            kod_formularza: Literal["PCC-3"] = "PCC-3"
            wariant_formularza: Literal[6] = 6
            cel_zlozenia: Annotated[CelZlozenia, form_field("P_6")]
            data_dokonania_czynnosci: Annotated[date, form_field("P_4")]
            kod_urzedu: Annotated[str, form_field("P_5")]
    
            @validator('data_dokonania_czynnosci')
            def validate_date(cls, v):
                if v < date(2024, 1, 1):
                    raise ValueError('Data musi być nie wcześniejsza niż 1 stycznia 2024')
                return v
    
        class Adres(BaseModel):
            kod_kraju: Annotated[str, form_field("P_8")]
            wojewodztwo: Annotated[Optional[str], form_field("P_9")] = Field(None, min_length=1, max_length=36)
            powiat: Annotated[Optional[str], form_field("P_10")] = Field(None, min_length=1, max_length=36)
            gmina: Annotated[Optional[str], form_field("P_11")] = Field(None, min_length=1, max_length=36)
            ulica: Annotated[Optional[str], form_field("P_12")] = Field(None, min_length=1, max_length=65)
            nr_domu: Annotated[str, form_field("P_13")] = Field(..., min_length=1, max_length=9)
            nr_lokalu: Annotated[Optional[str], form_field("P_14")] = Field(None, min_length=1, max_length=10)
            miejscowosc: Annotated[str, form_field("P_15")] = Field(..., min_length=1, max_length=56)
            kod_pocztowy: Annotated[Optional[str], form_field("P_16")] = None
    
            @validator('kod_pocztowy')
            def validate_kod_pocztowy(cls, v):
                if v is not None and not re.match(r'^\d\{2}-\d\{3}$', v):
                    raise ValueError('Nieprawidłowy format kodu pocztowego')
                return v
    
        class OsobaFizyczna(BaseModel):
            nip: Annotated[Optional[str], form_field("P_17")] = None
            pesel: Annotated[Optional[str], form_field("P_18")] = None
            imie_pierwsze: Annotated[str, form_field("P_19")] = Field(..., min_length=1, max_length=30)
            nazwisko: Annotated[str, form_field("P_20")] = Field(..., min_length=1, max_length=81)
            data_urodzenia: Annotated[date, form_field("P_21")]
            imie_ojca: Annotated[Optional[str], form_field("P_22")] = Field(None, min_length=1, max_length=30)
            imie_matki: Annotated[Optional[str], form_field("P_23")] = Field(None, min_length=1, max_length=30)
    
            @validator('nip')
            def validate_nip(cls, v):
                if v is not None and not re.match(r'^\d\{10}$', v):
                    raise ValueError('Nieprawidłowy format NIP')
                return v
    
            @validator('pesel')
            def validate_pesel(cls, v):
                if v is not None and not re.match(r'^\d\{11}$', v):
                    raise ValueError('Nieprawidłowy format PESEL')
                return v
    
        class OsobaNiefizyczna(BaseModel):
            nip: Annotated[str, form_field("P_24")]
            pelna_nazwa: Annotated[str, form_field("P_25")] = Field(..., min_length=1, max_length=240)
            skrocona_nazwa: Annotated[str, form_field("P_26")] = Field(..., min_length=1, max_length=70)
    
            @validator('nip')
            def validate_nip(cls, v):
                if not re.match(r'^\d\{10}$', v):
                    raise ValueError('Nieprawidłowy format NIP')
                return v
    
        class SectionB(BaseModel):
            osoba_fizyczna: Optional[OsobaFizyczna] = None
            osoba_niefizyczna: Optional[OsobaNiefizyczna] = None
            adres_zamieszkania_siedziby: Adres
            podmiot_skladajacy: Annotated[PodmiotSkladajacy, form_field("P_7")]
    
        class SectionC(BaseModel):
            przedmiot_opodatkowania: Annotated[PrzedmiotOpodatkowania, form_field("P_20")]
            miejsce_polozenia: Annotated[Optional[MiejscePolozenia], form_field("P_21")] = None
            miejsce_dokonania_czynnosci: Annotated[Optional[MiejscePolozenia], form_field("P_22")] = None
            tresc_czynnosci: Annotated[constr(max_length=2000), form_field("P_23")]
    
        class SectionD(BaseModel):
            podstawa_opodatkowania_1: Annotated[Optional[int], form_field("P_24")] = Field(None, ge=0)
            kwota_podatku_1: Annotated[Optional[int], form_field("P_25")] = Field(None, ge=0)
            podstawa_opodatkowania_2: Annotated[Optional[int], form_field("P_26")] = Field(None, ge=0)
            kwota_podatku_2: Annotated[Optional[int], form_field("P_27")] = Field(None, ge=0)
            podstawa_opodatkowania_zamiana: Annotated[Optional[int], form_field("P_28")] = Field(None, ge=0)
            stawka_podatku_zamiana: Annotated[Optional[int], form_field("P_29")] = Field(None, ge=0, le=100)
            kwota_podatku_zamiana: Annotated[Optional[int], form_field("P_30")] = Field(None, ge=0)
            podstawa_opodatkowania_pozyczka: Annotated[Optional[int], form_field("P_31")] = Field(None, ge=0)
            stawka_podatku_pozyczka: Annotated[Optional[float], form_field("P_32")] = Field(None, ge=0, le=100)
            kwota_podatku_pozyczka: Annotated[Optional[int], form_field("P_33")] = Field(None, ge=0)
            podstawa_opodatkowania_darowizna: Annotated[Optional[int], form_field("P_34")] = Field(None, ge=0)
            stawka_podatku_darowizna: Annotated[Optional[int], form_field("P_35")] = Field(None, ge=0, le=100)
            kwota_podatku_darowizna: Annotated[Optional[int], form_field("P_36")] = Field(None, ge=0)
            podstawa_opodatkowania_uzytkowanie: Annotated[Optional[int], form_field("P_37")] = Field(None, ge=0)
            stawka_podatku_uzytkowanie: Annotated[Optional[int], form_field("P_38")] = Field(None, ge=0, le=100)
            kwota_podatku_uzytkowanie: Annotated[Optional[int], form_field("P_39")] = Field(None, ge=0)
            podstawa_opodatkowania_hipoteka: Annotated[Optional[int], form_field("P_40")] = Field(None, ge=0)
            kwota_podatku_hipoteka: Annotated[Optional[int], form_field("P_41")] = Field(None, ge=0)
            kwota_podatku_hipoteka_nieustalona: Annotated[Optional[int], form_field("P_42")] = Field(None, ge=0)
            rodzaj_czynnosci_innej: Annotated[Optional[str], form_field("P_43A")] = None
            podstawa_opodatkowania_inna: Annotated[Optional[int], form_field("P_43")] = Field(None, ge=0)
            stawka_podatku_inna: Annotated[Optional[int], form_field("P_44")] = Field(None, ge=0, le=100)
            kwota_podatku_inna: Annotated[Optional[int], form_field("P_45")] = Field(None, ge=0)
            kwota_podatku_naleznego: Annotated[Optional[int], form_field("P_46")] = Field(None, ge=0)
    
        class SectionE(BaseModel):
            typ_spolki: Annotated[Optional[TypSpolki], form_field("P_47")] = None
            podstawa_opodatkowania: Annotated[Optional[PodstawaOpodatkowania], form_field("P_48")] = None
            kwota_podstawy_opodatkowania: Annotated[Optional[int], form_field("P_49")] = Field(None, ge=0)
            koszty: Annotated[Optional[float], form_field("P_50")] = Field(None, ge=0)
            podstawa_obliczenia_podatku: Annotated[Optional[float], form_field("P_51")] = Field(None, ge=0)
            kwota_podatku: Annotated[Optional[int], form_field("P_52")] = Field(None, ge=0)
    
        class SectionF(BaseModel):
            kwota_podatku_do_zaplaty: Annotated[int, form_field("P_53")] = Field(..., ge=0)
    
        class SectionG(BaseModel):
            wojewodztwo: Annotated[Optional[str], form_field("P_54")] = Field(None, min_length=1, max_length=36)
            powiat: Annotated[Optional[str], form_field("P_55")] = Field(None, min_length=1, max_length=36)
            gmina: Annotated[Optional[str], form_field("P_56")] = Field(None, min_length=1, max_length=36)
            ulica: Annotated[Optional[str], form_field("P_57")] = Field(None, min_length=1, max_length=65)
            nr_domu: Annotated[Optional[str], form_field("P_58")] = Field(None, min_length=1, max_length=9)
            nr_lokalu: Annotated[Optional[str], form_field("P_59")] = Field(None, min_length=1, max_length=10)
            miejscowosc: Annotated[Optional[str], form_field("P_60")] = Field(None, min_length=1, max_length=56)
            kod_pocztowy: Annotated[Optional[str], form_field("P_61")] = None
    
            @validator('kod_pocztowy')
            def validate_kod_pocztowy(cls, v):
                if v is not None and not re.match(r'^\d\{2}-\d\{3}$', v):
                    raise ValueError('Nieprawidłowy format kodu pocztowego')
                return v
    
        class SectionH(BaseModel):
            liczba_zalacznikow: Annotated[Optional[int], form_field("P_62")] = Field(None, ge=0)
    
        class Deklaracja(BaseModel):
            sekcja_a: SectionA
            sekcja_b: SectionB
            sekcja_c: SectionC
            sekcja_d: SectionD
            sekcja_e: SectionE
            sekcja_f: SectionF
            sekcja_g: Optional[SectionG] = None
            sekcja_h: Optional[SectionH] = None
            pouczenia: int = Literal[1]
    
        # Komentarz główny
        #Ten model Pydantic reprezentuje strukturę deklaracji PCC-3 (Podatek od czynności cywilnoprawnych).
        #Model został podzielony na sekcje odpowiadające głównym częściom formularza:
        #A. Nagłówek deklaracji
        #B. Dane podatnika
        #C. Przedmiot opodatkowania i treść czynności cywilnoprawnej
        #D. Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany
        #E. Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki
        #F. Podatek do zapłaty
        #G. Informacje dodatkowe
        #H. Informacja o załącznikach
        #
        #Każda sekcja jest reprezentowana przez osobną klasę, co ułatwia organizację i zrozumienie struktury formularza.
        #Dodatkowo, każde pole zawiera informację o numerze odpowiadającego mu pola w formularzu PCC-3.
        #
        #Model zawiera również walidacje zgodne z regułami określonymi w schemacie XSD, 
        #w tym ograniczenia dotyczące długości pól tekstowych, formatów danych (np. NIP, PESEL, kod pocztowy) 
        #oraz zakresów wartości liczbowych.
        #
        #Użyto dekoratora form_field do przechowywania numeru pola formularza dla każdego pola,
        #co jest zgodne z Pydantic v2 i pozwala na dodanie niestandardowych metadanych do pól.
        
        Current State
        {current_state}
        
        Your Tasks:
        1. Analyze the user's latest query and previous conversation.
        2. Extract all relevant information that fits the PCC-3 form structure.
        3. Validate the extracted data against the form's requirements.
        4. Respond with the most pertinent information related to the user's query.
        5. If any data doesn't meet validation criteria, explain the issue clearly.
        6. Provide guidance on correctly filling out the form when appropriate.
        7. Be explicit about errors provided by the users.
        
        Remember: Accuracy is crucial. Only include information explicitly provided by the user.
        """.replace("{current_state}", current_state)


def merge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge(result[key], value)
        elif value is not None:
            result[key] = value
        elif key not in result:
            result[key] = None
    return result


db = {}


@app.post("/chat")
async def answer_chat(req: Request):
    try:
        print(db.get(req.conv_id, {}))

        messages = [Message(role="system", content=get_system_prompt(req.declaration.model_dump_json()))] + req.messages

        be_model = db.get(req.conv_id, {})
        fe_model = req.declaration.model_dump()  # Convert Pydantic model to dict

        model = merge(be_model, fe_model)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            response_model=Response
        )

        try:
            # Merge and store as dict
            db[req.conv_id] = merge(model, response.declaration.model_dump())
        except Exception as e:
            print(e)

        print(db.get(req.conv_id, {}))

        return Response(
            response=response.response,
            declaration=db[req.conv_id]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temporary location
        temp_file_path = f"./temp/{file.filename}"
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)

        with open(temp_file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Call the OpenAI Whisper API
        with open(temp_file_path, "rb") as audio_file:
            response = OpenAI().audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text",
                language="pl",
            )

        # Clean up the temporary file
        os.remove(temp_file_path)

        return JSONResponse(content={"transcription": response})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/analyze-document")
async def analyze_document(
        file: UploadFile = File(...)
):
    prompt = "Analyze the document. Give me all key information. Don't mess up numbers. Answer in Polish."
    try:
        # Generate a random UUID and prepend it to the filename
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        temp_file_path = f"./temp/{unique_filename}"
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)

        with open(temp_file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        logger.info(f"Received file: {unique_filename}")
        logger.info(f"Prompt: {prompt}")

        analysis = process_document(temp_file_path, prompt)

        if analysis:
            logger.info("Document analysis successful")
            return {"analysis": analysis}
        else:
            logger.error("Failed to analyze the document")
            raise HTTPException(status_code=500, detail="Failed to analyze the document")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    print("running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
