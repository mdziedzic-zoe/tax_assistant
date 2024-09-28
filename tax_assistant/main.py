import os
from copy import deepcopy
from typing import List, Optional, Type, Any, Tuple, Literal, TypeVar

import instructor
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.params import File
from openai import OpenAI
from pydantic import BaseModel, create_model
from pydantic.fields import FieldInfo
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from tax_assistant.models.partial_taxform import PartialDeklaracja

load_dotenv()
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
    messages: List[Message]


class Response(BaseModel):
    response: str
    partial: PartialDeklaracja


system_prompt = """
    <mission>
        You are an expert in interpreting user input and extracting it into a structured data output. Your main focus is
         to be correct and never assume or deduce any information that were not explicitly mentioned in the conversation 
         with the user. Your answers should be in Polish only.
    </mission>
    <data-model>

    def form_field(form_field_number: str):
        def decorator(field: Field):
            field.json_schema_extra = {"form_field_number": form_field_number}
            return field
        return decorator

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
            if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
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
            if v is not None and not re.match(r'^\d{10}$', v):
                raise ValueError('Nieprawidłowy format NIP')
            return v

        @validator('pesel')
        def validate_pesel(cls, v):
            if v is not None and not re.match(r'^\d{11}$', v):
                raise ValueError('Nieprawidłowy format PESEL')
            return v

    class OsobaNiefizyczna(BaseModel):
        nip: Annotated[str, form_field("P_24")]
        pelna_nazwa: Annotated[str, form_field("P_25")] = Field(..., min_length=1, max_length=240)
        skrocona_nazwa: Annotated[str, form_field("P_26")] = Field(..., min_length=1, max_length=70)

        @validator('nip')
        def validate_nip(cls, v):
            if not re.match(r'^\d{10}$', v):
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
            if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
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
    </data-model>
    <tasks>         
         Respond with data most sensible to the users latest query.
         Analyse past conversation and extract data relevant to the data model. Ensure that validation constraints are met.
         When validation constraints are not met, highlight this in the user message.
    </tasks>     
    """


@app.post("/process_pcc3")
async def process_pcc3(req: Request):
    try:
        messages = [Message(role="system", content=system_prompt)] + req.messages
        print(messages)
        response = client.chat.completions.create(
            # model="gpt-4o",
            model="gpt-3.5-turbo",
            messages=messages,
            response_model=Response
        )
        print(response)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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


if __name__ == "__main__":
    import uvicorn
    print("running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
