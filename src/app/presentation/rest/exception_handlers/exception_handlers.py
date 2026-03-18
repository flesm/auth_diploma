from fastapi import FastAPI

from src.app.presentation.rest.exception_handlers import (
    auth_handlers,
    permission_handlers,
    role_handlers,
    users_handlers,
)


def setup_exception_handlers(app: FastAPI) -> None:
    all_handlers = [
        auth_handlers.handlers,
        users_handlers.handlers,
        permission_handlers.handlers,
        role_handlers.handlers,
    ]
    for handler_mapping in all_handlers:
        for exception, handler in handler_mapping.items():
            app.add_exception_handler(exception, handler)
