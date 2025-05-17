from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str
    chatgpt_model: str = "gpt-4o-mini"
    claude_model: str = "claude-3-7-sonnet-20250219"


class ChatResponse(BaseModel):
    prompt: str
    chatgpt_response: str
    claude_response: str
