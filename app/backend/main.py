from fastapi import FastAPI

app = FastAPI(
    title="AgriClimateAI",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AgriClimateAI"
    }

@app.get("/health")
def health():
    return {
        "status": "running"
    }