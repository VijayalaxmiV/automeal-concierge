from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AutoMeal Concierge",
    version="0.1.0",
    description="AI-powered multi-agent meal scheduling system",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Welcome to AutoMeal Concierge!"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "AutoMeal Concierge",
        "version": "0.1.0",
    }