# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chatbot")
async def chatbot(request: ChatRequest):
    user_message = request.message

    if "hello" in user_message.lower():
        reply = "Hi there! How can I help you?"
    elif "xin chào" in user_message.lower():
        reply = "Chào bạn! Tôi là chatbot hỗ trợ."
    else:
        reply = f"🤖 Bot nhận được: '{user_message}'"

    return JSONResponse(content={"text": reply})
