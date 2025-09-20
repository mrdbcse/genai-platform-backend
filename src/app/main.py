from fastapi import FastAPI

from src.app.router.med_bot import router as medbot_router

title = "Gen AI Platform Backend"
description = "This backend is the foundation for a robust, enterprise-grade GenAI platform. Each microservice addresses a unique business use case and exposes RESTful APIs, designed for secure deployment with Docker, Kubernetes, and Terraform on major cloud providers."
version = "1.0.0"

app = FastAPI(title=title, description=description, version=version, debug=True)

app.include_router(router=medbot_router)


@app.get("/")
async def home():
    return {
        "message": "Server is running",
        "title": title,
        "description": description,
        "version": version,
    }
