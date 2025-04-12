from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def root():
    return "Welcome to my Weather API"