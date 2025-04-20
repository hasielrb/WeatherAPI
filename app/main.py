from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import weather

app = FastAPI(
    title="Weather API",
    description="API to query weather data",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",          # Development
    "https://yourdomain.com",         # Production
    "https://app.yourdomain.com"      # Subdomain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"]
)

app.include_router(weather.router)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to Weather API",
        "example_request": {
            "endpoint": "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Cuba/2025-04-19/2025-04-22",
            "parameters": {
                "required": {
                    "location": "City, coordinates or address"
                },
                "optional": {
                    "start_date": "Start date (YYYY-MM-DD)",
                    "end_date": "End date (requires start_date)"
                }
            }
        },
        "try_it": "Visit /docs to interact with the API",
        "note": "If you only use start_date without end_date, you will get the forecast/historical for a single day."
    }