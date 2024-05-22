import uvicorn
from fastapi import FastAPI

from app.api_v1 import router as api_v1_router

app = FastAPI()
app.include_router(router=api_v1_router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
