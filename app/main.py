from fastapi import FastAPI, HTTPException, status
import requests

from core.config import settings
from models.weather import WeatherRequest

app = FastAPI()

@app.get("/", tags=["Root"])
async def root():
    return "Welcome to my Weather API"

@app.get("/weather", tags=["Weather"])
async def get_weather(parameters: WeatherRequest):
    try:
        url = f"{settings.BASE_URL}{parameters.location}"
        params = {
            "unitGroup": "metric",
            "contentType": "json",
            "key": settings.API_KEY
        }

        if (parameters.start_date):
            url += f"/{parameters.start_date}"

            if (parameters.end_date):
                url += f"/{parameters.end_date}"

        response = requests.get(url=url, params=params)
        response.raise_for_status()

        return response.json()
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error obtaining data")

