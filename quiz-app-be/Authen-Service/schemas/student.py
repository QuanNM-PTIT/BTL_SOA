from pydantic import BaseModel


class StudentInfo(BaseModel):
    student_code: str