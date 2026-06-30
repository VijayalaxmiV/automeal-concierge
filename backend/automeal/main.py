from fastapi import FastAPI

app = FastAPI(
    title="AutoMeal Concierge",
    version="0.1.0",
    description="AI-powered multi-agent meal scheduling system"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AutoMeal Concierge!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "AutoMeal Concierge",
        "version": "0.1.0"
    }