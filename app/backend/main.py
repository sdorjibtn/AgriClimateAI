from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_advisor.advisor import generate_advice

app = FastAPI(
    title="AgriClimateAI",
    version="0.1.0",
    description="AI agricultural advisor and climate intelligence platform"
)


class AdvisorRequest(BaseModel):
    question: str
    crop: str | None = None
    location: str | None = None


@app.get("/")
def root():
    return {
        "message": "Welcome to AgriClimateAI",
        "description": "AI agricultural advisor and climate intelligence platform"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.post("/advisor")
def advisor(request: AdvisorRequest):
    return generate_advice(
        question=request.question,
        crop=request.crop,
        location=request.location
    )