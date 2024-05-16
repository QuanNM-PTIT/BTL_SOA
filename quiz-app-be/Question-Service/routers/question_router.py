from fastapi import APIRouter
from schemas.question import CreateQuestion, GetQuestions
from models.question import Question

router = APIRouter(
    prefix="/question_service",
    tags=["question"]
)


@router.post("/create_question")
async def create_question(data: CreateQuestion):
    await Question.create(data)
    return {"message": "Question created successfully"}


@router.post("/get_questions")
async def get_questions(request: GetQuestions):
    questions = await Question.get_by_test_id(request)
    return {
        "status": "success",
        "data": questions,
    }
