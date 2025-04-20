from pydantic import BaseModel
from typing import Optional

class WeatherRequest(BaseModel):
    location: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
