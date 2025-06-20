from fastapi import FastAPI
from app.api import upload

app = FastAPI(title="Enterprise GenAI Knowledge Assistant", version="0.0.1")
app.include_router(upload.router, prefix="/api")
