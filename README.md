# Weather API 🌦️🔍

**Weather Project** | A REST API for accessing historical and forecast weather data using VisualCrossing

[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-%2347A248)](https://fastapi.tiangolo.com)
[![VisualCrossing](https://img.shields.io/badge/Weather_Data-VisualCrossing-%23007A8D)](https://www.visualcrossing.com)

## Key Features
- 🌍 Location-based weather queries (city, coordinates, address)
- 📅 Historical weather data and forecasts
- 📈 Date range support (start_date/end_date parameters)
- 🔐 Secure API key management
- 📦 Lightweight (~5ms response time)  
- 🛡️ CORS protection with configurable origins

## Tech Stack
- **Backend**: FastAPI
- **External API**: VisualCrossing Weather
- **Validation**: Pydantic models
- **Security**: Environment variables

## Quick Start

1. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Clone repo & install dependencies:
```bash
git clone https://github.com/hasielrb/WeatherAPI.git
cd WeatherAPI
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure environment variables
```bash
cp -n .env.example .env
nano .env
```
5. Run the application
```bash
cd app/
uvicorn main:app --reload
```
