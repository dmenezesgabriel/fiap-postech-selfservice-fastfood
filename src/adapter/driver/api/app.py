from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.adapter.driver.api.settings import Settings
from src.adapter.driver.api.api_v1.api import router as api_router


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
