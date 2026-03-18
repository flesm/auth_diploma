from typing import Any, AsyncGenerator, cast
from uuid import uuid4

import pytest
import pytest_asyncio
from faker import Faker
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert, text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

from src.app.container import Container
from src.app.infra.connection_engines.sqla.models import Base, Permission, Role
from src.app.presentation.rest.exception_handlers.exception_handlers import (
    setup_exception_handlers,
)
from src.app.presentation.rest.routes.v1 import v1_router
from src.tests.environment.config import FakeConfig


@pytest_asyncio.fixture
async def engine(fake_config: FakeConfig) -> AsyncGenerator[AsyncEngine, Any]:
    engine = create_async_engine(str(fake_config.DB.dsn), echo=True)
    try:
        yield engine
    finally:
        await engine.dispose()


@pytest_asyncio.fixture
async def app(
    engine: AsyncEngine, fake_config: FakeConfig
) -> AsyncGenerator[FastAPI, Any]:
    app = FastAPI()
    app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
    setup_exception_handlers(app)

    container = Container()
    container.config.override(fake_config)

    container.init_resources()
    container.wire(
        modules=[
            "src.app.presentation.rest.routes.v1.user.register.controllers",
            "src.app.presentation.rest.routes.v1.user.reset_password."
            "controllers",
            "src.app.presentation.rest.routes.v1.user.verify_email."
            "controllers",
            "src.app.presentation.rest.routes.v1.user.auth.controllers",
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
            "src.app.presentation.rest.routes.v1.user.profile." "controllers",
        ]
    )
    app.container = container
    yield app
    container.unwire()


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, Any]:
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://testserver"
    ) as ac:
        yield ac


@pytest.fixture
def async_session(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(engine, expire_on_commit=False)


@pytest.fixture
def url_v1() -> str:
    return "/api/v1"


@pytest_asyncio.fixture(autouse=True)
async def clean_db(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(table.delete())


@pytest_asyncio.fixture
async def another_regular_permission_id(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    permission_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(Permission).values(
                id=permission_id,
                name="name",
                description=faker.random_letter(),
            )
        )
        await session.commit()

    return cast(str, permission_id)


@pytest_asyncio.fixture
async def foreign_permission_id() -> str:

    permission_id = uuid4()

    return cast(str, permission_id)


@pytest_asyncio.fixture
async def another_regular_role_id(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    role_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(Role).values(
                id=role_id, name="name", description=faker.random_letter()
            )
        )
        await session.commit()

    return cast(str, role_id)


@pytest_asyncio.fixture
async def foreign_role_id() -> str:

    role_id = uuid4()

    return cast(str, role_id)


@pytest_asyncio.fixture(autouse=True)
async def seed_roles(engine: AsyncEngine) -> None:
    query = """
        INSERT INTO roles (id, name, description) VALUES
        ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'common', 'common user'),
        ('5fa85f64-5717-4562-b3fc-2c963f66afa6', 'admin', 'admin can do anything'),
        ('8fa85f64-5717-4562-b3fc-2c963f66afa6', 'superadmin', 'can create other admins')
        ON CONFLICT (id) DO NOTHING;
    """  # noqa: E501
    async with engine.begin() as conn:
        await conn.execute(text(query))
