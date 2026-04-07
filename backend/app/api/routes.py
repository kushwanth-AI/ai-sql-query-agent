from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import process_query

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def ask_question(request: QueryRequest):

    result = process_query(request.question)

    return result