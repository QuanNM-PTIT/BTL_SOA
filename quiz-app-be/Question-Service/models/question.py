import uuid
from umongo import Document, fields

from schemas.question import CreateQuestion, GetQuestions
from configs.database import question_instance

@question_instance.register
class Question(Document):
    test_id = fields.StringField(required=True)
    text = fields.StrField(required=True, max_length=1000)
    answers = fields.ListField(fields.DictField(), default=[])

    class Meta:
        collection_name = "questions"

    @classmethod
    async def create(cls, data: CreateQuestion):
        try:
            await cls.collection.insert_one(data.dict())
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    async def get_by_test_id(cls, request: GetQuestions):
        questions = await cls.collection.find({'test_id': request.test_id}).to_list(None)
        for question in questions:
            question["_id"] = str(question["_id"])
            answers = []
            for answer in question["answers"]:
                answers.append({
                    "text": answer["text"]
                })
            question["answers"] = answers
        return questions