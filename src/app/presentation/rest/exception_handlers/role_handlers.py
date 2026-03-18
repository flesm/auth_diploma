from fastapi import Request
from starlette.responses import JSONResponse

from src.app.application.use_cases.roles.exceptions import (
    RoleAlreadyExistException,
    RoleNotFoundException,
)


def role_already_exist_handler(
    request: Request, exc: RoleAlreadyExistException
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Role already exist."}
    )


def role_not_found_handler(
    request: Request, exc: RoleNotFoundException
) -> JSONResponse:
    return JSONResponse(status_code=400, content={"detail": "Role not found."})


handlers = {
    RoleAlreadyExistException: role_already_exist_handler,
    RoleNotFoundException: role_not_found_handler,
}
