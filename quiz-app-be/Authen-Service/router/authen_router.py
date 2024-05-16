from fastapi import APIRouter
from schemas.student import StudentInfo
from constants.all import QLDT_LOGIN_URL, QLDT_DSSV_URL
import httpx
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

router = APIRouter(
    prefix="/authen_service",
    tags=["Authen"]
)


@router.post("/validate_student")
async def validate_student(student: StudentInfo):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(
            QLDT_LOGIN_URL,
            data={
                "username": "B20DCCN214",
                "password": "Sonha2612@",
                "grant_type": "password"
            }
        )
        response = response.json()
        access_token = response.get("access_token")
        dssv = await client.post(
            QLDT_DSSV_URL,
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            json={"filter":{"id_to_hoc":"-7456098251519912771","id_sinh_hoat":""}}
        )
        dssv = dssv.json().get("data").get("ds_sinh_vien")
        for sv in dssv:
            if sv.get("ma_sinh_vien") == student.student_code:
                return {
                    "status": "success",
                    "message": "Student is valid"
                }

    return {
        "status": "failed",
        "message": "Student is invalid"
    }
