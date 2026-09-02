from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.analysis import run_analysis


app = FastAPI(
    title="Student Performance Analytics API",
    description="Student performance analysis using NumPy",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Student Performance Analytics API is running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/analysis")
def get_analysis():
    return run_analysis()