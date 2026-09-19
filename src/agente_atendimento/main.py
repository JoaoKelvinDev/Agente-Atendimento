from fastapi import FastAPI

from agente_atendimento.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/health")

def health() -> dict[str, str]:
    return {"status" : "ok"}