import os

from dotenv import load_dotenv
from flask import Flask, request
from openai import OpenAI
from anthropic import Anthropic

from app.models import ChatRequest, ChatResponse

load_dotenv()


app = Flask(__name__)


### Initialize OpenAI and Anthropic clients
chatgpt_client = OpenAI(api_key=os.getenv("openai_api_key"))
claude_client = Anthropic(api_key=os.getenv("anthropic_api_key"))


def chat_with_chatgpt(prompt: str = None, model: str = None) -> str | None:
    if not prompt or not model:
        return None
    try:
        completion = chatgpt_client.chat.completions.create(
            model=model, store=True, messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in chat_with_chatgpt: {e}")
        return None


def chat_with_claude(prompt: str = None, model: str = None) -> str | None:
    if not prompt or not model:
        return None
    try:
        message = claude_client.messages.create(
            model=model, max_tokens=1024, messages=[{"role": "user", "content": prompt}]
        )
        return "".join(response.text for response in message.content)
    except Exception as e:
        print(f"Error in chat_with_claude: {e}")
        return None


@app.route("/chat", methods=["POST"])
def chat():
    chat_request = ChatRequest(**request.get_json())
    chatgpt_response = chat_with_chatgpt(
        chat_request.prompt, chat_request.chatgpt_model
    )
    claude_response = chat_with_claude(chat_request.prompt, chat_request.claude_model)
    return ChatResponse(
        prompt=chat_request.prompt,
        chatgpt_response=chatgpt_response,
        claude_response=claude_response,
    ).model_dump_json()
