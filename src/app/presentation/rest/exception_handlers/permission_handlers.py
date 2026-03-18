from fastapi import Request
from starlette.responses import JSONResponse

from src.app.application.use_cases.permissions.exceptions import (
    PermissionAlreadyExistException,
    PermissionNotFoundException,
)


def permission_already_exist_handler(
    request: Request, exc: PermissionAlreadyExistException
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Permission already exist."}
    )


def permission_not_found_handler(
    request: Request, exc: PermissionNotFoundException
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Permission not found."}
    )


handlers = {
    PermissionAlreadyExistException: permission_already_exist_handler,
    PermissionNotFoundException: permission_not_found_handler,
}
