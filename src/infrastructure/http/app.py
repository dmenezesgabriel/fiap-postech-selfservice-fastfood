from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.domain.base.exceptions import UserAlreadyExistsError
from src.infrastructure.http.api_v1.api import router as api_router
from src.infrastructure.http.settings import Settings

settings = Settings()


@lru_cache()
def get_settings():
    return settings.Settings()


app = FastAPI(
    title=settings.title,
    version=settings.version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    openapi_url=settings.openapi_url,
    root_path=settings.root_path,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


# Adding global exception handlers


@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(
        status_code=500,
        content={"message": f"{base_error_message}. Detail: {err}"},
    )


@app.exception_handler(UserAlreadyExistsError)
async def unicorn_exception_handler(
    request: Request, exc: UserAlreadyExistsError
):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
