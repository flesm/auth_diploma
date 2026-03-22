from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.presentation.rest.admin.admin_setup import setup_admin
from src.app.config import Config
from src.app.container import Container
from src.app.presentation.rest.exception_handlers.exception_handlers import (
    setup_exception_handlers,
)
from src.app.presentation.rest.routes.v1 import v1_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    container = Container()
    container.config.override(Config())
    container.init_resources()

    engine = container.db.container.db().engine

    setup_admin(app, engine)

    container.wire(
        modules=[
            "src.app.presentation.rest.routes.v1.user.register.controllers",
            "src.app.presentation.rest.routes.v1.user.reset_password."
            "controllers",
            "src.app.presentation.rest.routes.v1.user.verify_email."
            "controllers",
            "src.app.presentation.rest.routes.v1.user.auth.controllers",
            "src.app.presentation.rest.routes.v1.user.profile.controllers",
            "src.app.presentation.rest.routes.v1.permission.get.controllers",
            "src.app.presentation.rest.routes.v1.permission.create."
            "controllers",
            "src.app.presentation.rest.routes.v1.permission.update."
            "controllers",
            "src.app.presentation.rest.routes.v1.permission.delete."
            "controllers",
            "src.app.presentation.rest.routes.v1.role.get.controllers",
            "src.app.presentation.rest.routes.v1.role.create.controllers",
            "src.app.presentation.rest.routes.v1.role.update.controllers",
            "src.app.presentation.rest.routes.v1.role.delete.controllers",
            "src.app.presentation.rest.routes.v1.role_permission.attach."
            "controllers",
            "src.app.presentation.rest.routes.v1.role_permission.detach."
            "controllers",
        ]
    )

    app.container = container

    yield

    container.unwire()
    await container.shutdown_resources()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_exception_handlers(app)

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
