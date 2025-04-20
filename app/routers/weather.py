from fastapi import APIRouter, HTTPException, status
import requests
from core.config import settings
from models.weather import WeatherRequest

router = APIRouter()

@router.get("/weather", tags=["Weather"])
async def get_weather(parameters: WeatherRequest):
    try:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{parameters.location}"
        params = {
            "unitGroup": "metric",
            "contentType": "json",
            "key": settings.API_KEY
        }

        if (parameters.start_date): #2017-02-03
            url += f"/{parameters.start_date}"

            if (parameters.end_date):
                url += f"/{parameters.end_date}"

        response = requests.get(url=url, params=params)
        response.raise_for_status()
        
        print(url)
        return response.json()
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error obtaining data")
