from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from schemas.task import StartTest
from constants.all import QUESTION_SERVICE_URL, TEST_SERVICE_URL, STUDENT_SERVICE_URL, AUTHEN_SERVICE_URL
from configs.socket_manager import ConnectionManager
import httpx
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

router = APIRouter(
    prefix="/task_service",
    tags=["task"]
)

manager = ConnectionManager()


@router.websocket("/ws/status/{student_code}")
async def websocket_endpoint(websocket: WebSocket, student_code: str):
    await manager.connect(websocket, student_code)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(data, student_code)
    except WebSocketDisconnect:
        manager.disconnect(student_code)


async def authen_user(student_code):
    async with httpx.AsyncClient(verify=False) as client:
        await manager.send_personal_message("Start authenticating...", student_code)

        print(1)

        authen_response = await client.post(
            url=f'{AUTHEN_SERVICE_URL}/validate_student',
            json={"student_code": student_code}
        )

    if authen_response.status_code != 200 or authen_response.json()["status"] == "failed":
        return {
            "status": "failed",
            "message": "Student code is invalid!"
        }

    return {
        "status": "success",
        "message": "Student code is valid!"
    }


@router.post("/start_test")
async def start_test(data: StartTest):
    async with httpx.AsyncClient(verify=False) as client:
        await manager.send_personal_message("Start authenticating...", data.student_code)

        authen_response = await client.post(
            url=f'{AUTHEN_SERVICE_URL}/validate_student',
            json={"student_code": data.student_code}
        )

    if authen_response.status_code != 200 or authen_response.json()["status"] == "failed":
        return {
            "status": "failed",
            "message": "Student code is invalid!"
        }

    async with httpx.AsyncClient(verify=False) as client:
        await manager.send_personal_message("Start getting student info...", data.student_code)

        student_response = await client.post(
            url=f'{STUDENT_SERVICE_URL}/get_student',
            json={"student_code": data.student_code}
        )

    if student_response.status_code != 200:
        return {
            "status": "failed",
            "message": "Student code is invalid!"
        }

    async with httpx.AsyncClient(verify=False) as client:
        await manager.send_personal_message("Start getting test info...", data.student_code)

        test_response = await client.post(
            url=f'{TEST_SERVICE_URL}/get_test',
            json={"id": data.test_id}
        )

    if test_response.status_code != 200:
        return {
            "status": "failed",
            "message": "Test not found!"
        }

    test = test_response.json()["data"]
    student = student_response.json()["data"]
    if student.get('student_code') not in test['list_student']:
        return {
            "status": "failed",
            "message": "Student do not have access to this test!"
        }


    async with httpx.AsyncClient(verify=False) as client:
        await manager.send_personal_message("Start getting questions...", data.student_code)

        questions_response = await client.post(
            url=f'{QUESTION_SERVICE_URL}/get_questions',
            json={"test_id": data.test_id}
        )

    if questions_response.status_code != 200:
        return {
            "status": "failed",
            "message": "Questions not found!"
        }
    return {
        "status": "success",
        "data": {
            "test": test_response.json()["data"],
            "questions": questions_response.json()["data"],
            "student": student_response.json()["data"]
        }
    }

