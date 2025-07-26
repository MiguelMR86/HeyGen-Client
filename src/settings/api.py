import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HEYGEN_API_KEY")
BASE_API_URL = "https://api.heygen.com"

API_URLS = {
    "v1": f"{BASE_API_URL}/v1",
    "v2": f"{BASE_API_URL}/v2",
}

UPLOAD_URL = "https://upload.heygen.com/v1"
