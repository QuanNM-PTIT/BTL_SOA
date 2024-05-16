from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

FAPP_PORT = os.getenv("FAPP_PORT")
MONGODB_URL = os.getenv("MONGODB_URL")
QUESTION_SERVICE_URL = os.getenv("QUESTION_SERVICE_URL")