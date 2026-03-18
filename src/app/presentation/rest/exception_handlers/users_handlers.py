from fastapi import Request
from starlette.responses import JSONResponse

from src.app.application.use_cases.users.exceptions import (
    UserAlreadyVerifiedException,
    UserNotFound,
)
from src.app.application.use_cases.users.register.exceptions import (
    EmailAlreadyRegisteredException,
)


def user_not_found_handler(
    request: Request, exc: UserNotFound
) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": "User not found."})


def user_already_verified_handler(
    request: Request, exc: UserAlreadyVerifiedException
) -> JSONResponse:
    return JSONResponse(
        status_code=409, content={"detail": "User already verified."}
    )


def email_already_registered_handler(
    request: Request, exc: EmailAlreadyRegisteredException
) -> JSONResponse:
    return JSONResponse(
        status_code=409, content={"detail": "Email already registered."}
    )


handlers = {
    UserNotFound: user_not_found_handler,
    EmailAlreadyRegisteredException: email_already_registered_handler,
    UserAlreadyVerifiedException: user_already_verified_handler,
}
