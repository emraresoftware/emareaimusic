# Emare AI Music — API v1 Router

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "Emare AI Music API v1", "status": "active"}


@api_router.get("/info")
async def info():
    return {
        "app": "Emare AI Music",
        "version": "0.1.0",
        "category": "Platform",
    }
