from starlette.requests import Request
from starlette.responses import JSONResponse

from src.core.domain.exceptions import (
    EntityAlreadyExistsError,
    NotFoundError,
    UserAlreadyExistsError,
)


def register_exceptions(app):
    @app.exception_handler(Exception)
    async def validation_exception_handler(request, err):
        base_error_message = (
            f"Failed to execute: {request.method}: {request.url}"
        )
        return JSONResponse(
            status_code=500,
            content={"message": f"{base_error_message}. Detail: {err}"},
        )

    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        request: Request, exc: UserAlreadyExistsError
    ):
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(EntityAlreadyExistsError)
    async def entity_already_exists_handler(
        request: Request, exc: EntityAlreadyExistsError
    ):
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )
