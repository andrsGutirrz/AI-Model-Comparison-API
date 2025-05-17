import os

from dotenv import load_dotenv
from flask import Flask, request
from openai import OpenAI
from pydantic import BaseModel
from anthropic import Anthropic

load_dotenv()


class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    prompt: str
    chatgpt_response: str
    claude_response: str


app = Flask(__name__)


chatgpt_client = OpenAI(
  api_key=os.getenv("openai_api_key")
)
claude_client = Anthropic(api_key=os.getenv("anthropic_api_key"))


def chat_with_chatgpt(prompt: str = None) -> str | None:
    if not prompt:
        return None
    try:
        completion = chatgpt_client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in chat_with_chatgpt: {e}")
        return None


def chat_with_claude(prompt: str = None) -> str | None:
    if not prompt:
        return None
    try:
        message = claude_client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return "".join(response.text for response in message.content)
    except Exception as e:
        print(f"Error in chat_with_claude: {e}")
        return None


@app.route("/chat", methods=["POST"])
def chat():
    chat_request = ChatRequest(**request.get_json())
    chatgpt_response = chat_with_chatgpt(chat_request.prompt)
    claude_response = chat_with_claude(chat_request.prompt)
    return ChatResponse(
        prompt=chat_request.prompt,
        chatgpt_response=chatgpt_response,
        claude_response=claude_response
    ).model_dump_json()
