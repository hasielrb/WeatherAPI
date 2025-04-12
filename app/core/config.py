from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str
    BASE_URL: str

settings = Settings()