import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import instructor

from models.taxform import PCC3Form, Address, Taxpayer, TransactionDetails
load_dotenv()
client = instructor.from_openai(OpenAI())
app = FastAPI()

class Message(BaseModel):
    role: str
    content: str


class ConversationRecord(BaseModel):
    messages: List[Message]


class PCC3Request(BaseModel):
    pcc3_form: PCC3Form
    conversation: ConversationRecord


class PCC3Response(BaseModel):
    analysis: str = Field(..., description="Analysis of the PCC3 form and conversation")
    updated_form: PCC3Form = Field(..., description="Potentially updated PCC3 form based on the conversation")


@app.post("/process_pcc3")
async def process_pcc3(request: PCC3Request):
    # Prepare the messages for OpenAI
    messages = [
        {"role": "system",
         "content": "You are a helpful assistant processing PCC3 tax forms. Analyze the form and conversation, then provide an analysis and an updated form if necessary."},
        {"role": "user", "content": f"Here's the PCC3 form data: {request.pcc3_form.model_dump_json()}"}
    ]

    messages.extend([msg.dict() for msg in request.conversation.messages])

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            response_model=PCC3Response
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
