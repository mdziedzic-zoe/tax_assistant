import logging
import os
import uuid
from dataclasses import replace
from os import system
from typing import List

import instructor
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.params import File
from openai import OpenAI
from pydantic import BaseModel, ValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from tax_assistant.documents import process_document
from tax_assistant.models.grounding import brochure, circumstances
from tax_assistant.models.partial_taxform import PartialDeklaracja
from tax_assistant.models.taxform import Deklaracja
from tax_assistant.xml_gen import generate_xml

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
    generated_xml: str | None = None


def get_system_prompt(current_state):
    return r"""
You are an AI assistant specialized in Polish tax forms, particularly the PCC-3 form for civil law transactions tax. Your primary function is to interpret user input and extract relevant information to fill out the PCC-3 form accurately. Respond only in Polish.

<KEY-GUIDELINES>
- Extract only explicitly mentioned information from the user's input.
- Never assume or deduce information not directly stated.
- Ensure all extracted data adheres to the validation rules of the PCC-3 form.
- Highlight any validation issues in your response.
- Provide clear, concise responses focused on the user's most recent query.
- Consider the entire conversation history when extracting information.
- data_dokonania_czynnosci must be only set if the user mentions this.
- Ask user to verify the amount of podstawa_opodatkowania that you have found.
- Today is 29 Sep 2024, compute all relative dates e.g. yesterday relative to 29 Sep 2024.
- Always refer to CURRENT_STATE when deciding what to ask for next. Evaluate whether missing data requires additional prompting.
- Date format should be DD.MM.YYYY
- Ask for an appropriate Tax Office. List ones that are closest to the input. Make sure it belongs to the list supplied in TAX_OFFICES. Use the 6 character mapping provided in TAX_OFFICES.
</KEY_GUIDELINES>

<TAX_FORMS_DETAILS>
{brochure}
<TAX_FORMS_DETAILS>
<TAX_FORM_CIRCUMSTANCES>
{circumstances}
<TAX_FORM_CIRCUMSTANCES>

<CURRENT_STATE>
{current_state}
</CURRENT_STATE>

<TASKS>
1. Analyze the user's latest query and previous conversation.
2. Extract all relevant information that fits the PCC-3 form structure.
3. Validate the extracted data against the form's requirements.
4. Respond with the most pertinent information related to the user's query.
5. If any data doesn't meet validation criteria, explain the issue clearly.
6. Provide guidance on correctly filling out the form when appropriate.
7. Be explicit about errors provided by the users.
8. Set is_completed field inside each sekcja ONLY if all the required fields for xml generation inside given sekcja are filled!!!
9. In SectionB double check that podmiot has been correctly assigned.
10. In SectionD double check that podmiot 
"
</TASKS>

<CRUCIAL_REMINDERS>
1. REMEMBER: Accuracy is crucial. Only include information explicitly provided by the user.
2. Always end with prompt for filling data that's missing in the data model.
3. Focus on the total market value of the bought item, summing up all the sums mentioned.
4. Only set the data if mentioned by the user.
5. IMPORTANT: Before confirming completion of the form, do a thorough review of missing fields.
<CRUCIAL_REMINDERS>
""".replace("{current_state}", current_state).replace("{brochure}", brochure).replace("{circumstances}",
                                                                                      circumstances)


def get_init_system_prompt():
    return r"""
You are an AI assistant specialized in Polish tax forms, particularly the PCC-3 form for civil law transactions tax. Respond only in Polish using markdown format. 

<KEY-GUIDELINES>
- Using the brochure supplied, outline a very specific agenda detailing at least 3 steps. In the steps mention: 
    - why and who should submit that particular tax form and whether they are applicable.
    - what are the necessary information
    - What information has been gathered already 
- Extract only explicitly mentioned information from the user's input.
- Never assume or deduce information not directly stated.
- Ask user to verify the amount of podstawa_opodatkowania that you have found.
- Today is 29 Sep 2024, compute all relative dates e.g. yesterday relative to 29 Sep 2024. Ask the user for date confirmation.
- Focus on the total market value of the bought item, summing up all the sums mentioned. There may be more than a single numerical value provided.
</KEY_GUIDELINES>

IMPORTANT: Before returning with an answer, double check whether all KEY-GUIDELINES have been met. Ensure that the agenda is present and has at least 3 steps which are outlined in the response.

BROCHURE:
{brochure}
CIRCUMSTANCES:
{circumstances}
""".replace(f"{brochure}", brochure).replace(f"{circumstances}", circumstances)


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


def are_all_sections_complete(merged):
    required_sections = ['sekcja_a', 'sekcja_b', 'sekcja_c', 'sekcja_d']
    if not merged:
        return False
    for section in required_sections:
        if section not in merged or merged[section] is None or 'is_complete' not in merged[section]:
            return False
        if not merged[section]['is_complete']:
            return False

    return True


db = {}
messages_db = {}


@app.post("/chat")
async def answer_chat(req: Request):
    messages_db[req.conv_id] = messages_db.get(req.conv_id, [])

    # different case for initial round
    # if len(messages_db[req.conv_id]) == 0:
    #     print("init prompt")
    #     system_prompt = get_init_system_prompt()
    # else:

    system_prompt = get_system_prompt(req.declaration.model_dump_json())
    messages_db[req.conv_id].extend(req.messages)

    try:
        messages = [Message(role="system", content=system_prompt)] + messages_db[req.conv_id]

        be_model = db.get(req.conv_id, {})
        fe_model = req.declaration.model_dump()  # Convert Pydantic model to dict

        model = merge(be_model, fe_model)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            response_model=Response
        )

        messages_db[req.conv_id].append(Message(role="assistant", content=response.response))

        print(messages_db[req.conv_id])

        # Merge and store as dict
        merged = merge(model, response.declaration.model_dump())
        db[req.conv_id] = merged

        if are_all_sections_complete(merged):
            try:
                d = Deklaracja.model_validate(db[req.conv_id])
                xml = generate_xml(d)
                return Response(
                    response=response.response,
                    declaration=db[req.conv_id],
                    generated_xml=xml
                )

            except ValidationError as ve:
                print(ve)
                for e in ve.errors():
                    print(e)

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages + Message(role="user",
                                                content=f"There are some errors in the provided final configuration. Ask the user to fill in the data to address them. Here are the issues: {"\n".join(ve.errors()[:3])}"),
                    response_model=Response
                )

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

# # Ask gpt-4o-mini to answer with a number of a Urzad Skarbowy from the following list based on the user query. If there's no mention about any Urzad Skarbowy, return None.
# urzad_skarbowy_map_text = """
#         nazwa - kod_urzedu
#         Urzad Skarbowy Warszawa-Centrum - 123
#         Urzad Skarbowy Krakow-Nowa Huta - 124
#         Urzad Skarbowy Wroclaw-Fabryczna - 125
#         Urzad Skarbowy Poznan-Jezyce - 126
#         Urzad Skarbowy Gdansk-Polnoc - 127
#         """
#
# # Create a prompt to ask gpt-4o-mini
# urzad_skarbowy_prompt = f"""
#         Based on the user query, identify the kod_urzedu from the following list:
#         {urzad_skarbowy_map_text}
#         If there's no mention of any Urzad Skarbowy, return None.
#         User query: {req.messages[-1].content}
#         """
#
# urzad_skarbowy_response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": urzad_skarbowy_prompt}]
# )
#
# print(f"Identified Urzad Skarbowy number: {urzad_skarbowy_response}")
