from pydantic import BaseModel


class CreateStudent(BaseModel):
    student_code: str
    name: str


class GetStudent(BaseModel):
    student_code: str
