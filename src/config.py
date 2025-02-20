import os

from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENV", "dev")
debug = os.getenv("DEBUG", True) == "true"
secret_key = os.getenv('SECRET_KEY')    

app_host = os.getenv("APP_HOST")
app_port = os.getenv("APP__PORT")
app_root = os.getenv("APP_ROOT")
app_path = os.getenv("APP_PATH")
app_url = os.getenv("BASE_URL")

api_key = os.getenv("APOD_API_KEY")
apod_url = os.getenv("APOD_API_URL")
