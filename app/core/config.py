from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_KEY: str
    BASE_URL: str

settings = Settings()

