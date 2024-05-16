from fastapi import APIRouter
from schemas.student import CreateStudent, GetStudent
from models.student import Student

router = APIRouter(
    prefix="/student_service",
    tags=["student"]
)


@router.post("/create_student")
async def create_student(data: CreateStudent):
    await Student.create(data)
    return {"message": "Student created successfully"}


@router.post("/get_student")
async def get_student(request: GetStudent):
    student = await Student.get_by_test_student_code(request)
    return {
        "status": "success",
        "data": student,
    }
