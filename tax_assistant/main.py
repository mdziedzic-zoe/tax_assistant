import os
from copy import deepcopy

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, create_model
from typing import List, Optional, Type, Any, Tuple, Literal
from dotenv import load_dotenv
from openai import OpenAI
import instructor
from pydantic.fields import FieldInfo
from pydantic.v1.main import ModelMetaclass

from models.taxform import Deklaracja
from tax_assistant.models.taxform import SectionA, SectionB, SectionC, SectionD, SectionE, SectionF, SectionG, SectionH


def partial_model(model: Type[BaseModel]):
    def make_field_optional(field: FieldInfo, default: Any = None) -> Tuple[Any, FieldInfo]:
        new = deepcopy(field)
        new.default = default
        new.annotation = Optional[field.annotation]  # type: ignore
        return new.annotation, new

    return create_model(
        f'Partial{model.__name__}',
        __base__=model,
        __module__=model.__module__,
        **{
            field_name: make_field_optional(field_info)
            for field_name, field_info in model.model_fields.items()
        }
    )


@partial_model
class PSectionA(SectionA):
    pass


@partial_model
class PSectionB(SectionB):
    pass


@partial_model
class PSectionC(SectionC):
    pass


@partial_model
class PSectionD(SectionD):
    pass


@partial_model
class PSectionE(SectionE):
    pass


@partial_model
class PSectionF(SectionF):
    pass


@partial_model
class PSectionG(SectionG):
    pass


@partial_model
class PSectionH(SectionH):
    pass


@partial_model
class PartialDeklaracja(Deklaracja):
    sekcja_a: PSectionA
    sekcja_b: PSectionB
    sekcja_c: PSectionC
    sekcja_d: PSectionD
    sekcja_e: PSectionE
    sekcja_f: PSectionF
    sekcja_g: PSectionG = None
    sekcja_h: PSectionH = None
    pouczenia: int = Literal[1]


load_dotenv()
client = instructor.from_openai(OpenAI())
app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ConversationRecord(BaseModel):
    messages: List[Message]


@app.post("/process_pcc3")
async def process_pcc3():
    # Prepare the messages for OpenAI
    messages = [
        {"role": "system",
         "content": "Answer in Polish only. Interpret incoming information and input the into the taxdata formula. Do not fill in the data you've got no context on. Refrain from filling in data you have no context on. Fill in missing data with 'NO_DATA'. Refrain from adding dates or doing any calulcations. "},
        {"role": "user",
         "content": "Wczoraj kupiłem na giełdzie samochodowej Fiata 126p rok prod. 1975, kolor zielony. Przejechane ma 1000000 km, idzie jak przecinak, nic nie stuka, nic nie puka, dosłownie igła. Zapłaciłem za niego 1000zł ale jego wartość jest wyższa o 2000 zł i co mam z tym zrobić ?"
         }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            response_model=PartialDeklaracja
        )
        print(response)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    pd = PartialDeklaracja(sekcja_a=PSectionA())

    print(pd)
    print("running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
