from bson import ObjectId
from umongo import Document, fields
from schemas.test import CreateTest, GetTest
from configs.database import test_instance

@test_instance.register
class Test(Document):
    name = fields.StringField(required=True)
    time = fields.IntField(required=True)
    list_students = fields.ListField(fields.StringField(), default=[])

    class Meta:
        collection_name = "tests"

    @classmethod
    async def create(cls, data: CreateTest):
        try:
            await cls.collection.insert_one(data.dict())
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    async def get_test_by_id(cls, request: GetTest):
        test = await cls.collection.find_one({"_id": ObjectId(request.id)})
        return test