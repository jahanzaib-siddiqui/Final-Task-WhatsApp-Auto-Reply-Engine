from fastapi import FastAPI
from pydantic import BaseModel

from chatbot_engine import AutoReplyEngine


app = FastAPI(
    title="NitroXhift WhatsApp Auto-Reply Engine"
)


engine = AutoReplyEngine(
    "../data/faq_dataset.csv"
)


class MessageRequest(BaseModel):

    message: str


@app.get("/")
def home():

    return {
        "message":
        "NitroXhift WhatsApp Auto-Reply Engine is running"
    }


@app.post("/reply")
def get_reply(request: MessageRequest):

    result = engine.get_response(
        request.message
    )

    return result