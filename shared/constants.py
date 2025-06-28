import os
from dotenv import load_dotenv

load_dotenv()

TEST_SUIT_NAME = "Bitnami Opencart Eshop"
ESHOP_BASE_URL = os.getenv("OPENCART_HOST", "localhost:8081")
