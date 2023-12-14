from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.adapter.driver.api.settings import Settings
from src.adapter.driver.api.api_v1.api import router as api_router

from src.core.domain.base.exceptions import InvalidCpfError


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

# TODO : Buisiness Execptio, Service Exception, etc...
## Adding global exception handlers

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=500, content={"message": f"{base_error_message}. Detail: {err}"})
@app.exception_handler(InvalidCpfError)
async def unicorn_exception_handler(request: Request, exc: InvalidCpfError):
    return JSONResponse(
        status_code=422,
        content={
            "message":"Error message here"
            # "message": f"Oops! {exc.message}.",
            # "error_code": exc.error_code,
            # "error": exc.error
        },
    )
