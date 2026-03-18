from fastapi import Request
from starlette.responses import JSONResponse

from src.app.application.use_cases.users.auth.login.exceptions import (
    InvalidCredentialsException,
)
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
)
from src.app.application.use_cases.users.reset_password.exceptions import (
    InvalidOrExpiredResetLink,
)


def invalid_reset_link_handler(
    request: Request, exc: InvalidOrExpiredResetLink
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Invalid or expired reset link."}
    )


def invalid_or_expired_token_handler(
    request: Request, exc: InvalidOrExpiredTokenException
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Invalid or expired token."}
    )


def invalid_credentials_handler(
    request: Request, exc: InvalidCredentialsException
) -> JSONResponse:
    return JSONResponse(
        status_code=400, content={"detail": "Invalid credentials."}
    )


handlers = {
    InvalidOrExpiredResetLink: invalid_reset_link_handler,
    InvalidOrExpiredTokenException: invalid_or_expired_token_handler,
    InvalidCredentialsException: invalid_credentials_handler,
}
