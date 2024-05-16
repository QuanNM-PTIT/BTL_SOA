import uvicorn
from fastapi import FastAPI
from routers.test_router import router as test_router
from starlette.middleware.cors import CORSMiddleware
from constants import FAPP_PORT

app = FastAPI()

app.include_router(test_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=int(FAPP_PORT))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
