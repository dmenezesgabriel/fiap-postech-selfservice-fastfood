import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse


if __name__ == "__main__":
    uvicorn.run(
        "src.adapter.driver.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

