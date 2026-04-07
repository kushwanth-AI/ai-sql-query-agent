from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI SQL Agent",
    description="Natural Language to PostgreSQL using LangGraph + Gemini",
)

@app.get("/")
def root():
    return {"message": "AI SQL Agent is running"}

app.include_router(router)