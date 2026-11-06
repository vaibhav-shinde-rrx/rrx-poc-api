from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class EchoRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/echo")
def echo(body: EchoRequest):
    text = body.text
    return {
        "response": f"Backend received: {text} ({len(text)} characters)",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
