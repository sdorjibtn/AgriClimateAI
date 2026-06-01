from app.crop_engine.crop_suitability import assess_crop_suitability
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_advisor.advisor import generate_advice

app = FastAPI(
    title="AgriClimateAI",
    version="0.1.0",
    description="AI agricultural advisor and climate intelligence platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AdvisorRequest(BaseModel):
    question: str
    crop: str | None = None
    location: str | None = None

class CropSuitabilityRequest(BaseModel):
    crop: str
    location: str

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

@app.post("/crop-suitability")
def crop_suitability(request: CropSuitabilityRequest):
    return assess_crop_suitability(
        crop=request.crop,
        location=request.location
    )

