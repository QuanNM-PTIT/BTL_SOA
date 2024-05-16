from pydantic import BaseModel


class StartTest(BaseModel):
    test_id: str
    student_code: str