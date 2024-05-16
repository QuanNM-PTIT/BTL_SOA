from pydantic import BaseModel


class CreateTest(BaseModel):
    name: str
    time: int
    list_student: list[str]


class GetTest(BaseModel):
    id: str