from fastapi import APIRouter
from schemas.test import CreateTest, GetTest
from models.test import Test
from constants.all import QUESTION_SERVICE_URL
import httpx

router = APIRouter(
    prefix="/test_service",
    tags=["test"]
)


@router.post("/create_test")
async def create_test(data: CreateTest):
    await Test.create(data)
    return {"message": "Test created successfully"}


@router.post("/get_test")
async def get_test(request: GetTest):
    test = await Test.get_test_by_id(request)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f'{QUESTION_SERVICE_URL}/get_questions',
            json={"test_id": str(test["_id"])}
        )
    test["_id"] = str(test["_id"])
    return {
        "status": "success",
        "data": {
            "test": test,
            "questions": response.json()["data"]
        },
    }

