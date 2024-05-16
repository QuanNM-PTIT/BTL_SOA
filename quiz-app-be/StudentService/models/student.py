import uuid
from umongo import Document, fields

from schemas.student import CreateStudent, GetStudent
from configs.database import student_instance


@student_instance.register
class Student(Document):
    student_code = fields.StringField(required=True, unique=True)
    student_name = fields.StringField(required=True)

    class Meta:
        collection_name = "students"

    @classmethod
    async def create(cls, data: CreateStudent):
        try:
            await cls.collection.insert_one(data.dict())
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    async def get_by_test_student_code(cls, request: GetStudent):
        student = await cls.collection.find_one({'student_code': request.student_code})
        if student:
            student["_id"] = str(student["_id"])
            return student
        else:
            return {}

