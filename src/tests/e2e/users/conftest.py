from typing import cast
from uuid import uuid4

import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from src.app.infra.connection_engines.sqla.models import User
from src.app.infra.jwt.jwt_encoder import JwtTokenEncoder
from src.tests.environment.config import FakeConfig


@pytest.fixture
def async_session(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(engine, expire_on_commit=False)


@pytest_asyncio.fixture
async def unverified_regular_user(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    email = faker.unique.email()

    async with async_session() as session:
        await session.execute(
            insert(User).values(
                id=uuid4(),
                email=email,
                hashed_password=faker.password(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                is_verified=False,
                is_active=True,
                role_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            )
        )
        await session.commit()

    return cast(str, email)


@pytest_asyncio.fixture
async def verified_regular_user(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    email = faker.unique.email()

    async with async_session() as session:
        await session.execute(
            insert(User).values(
                id=uuid4(),
                email=email,
                hashed_password=faker.password(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                is_verified=True,
                is_active=True,
                role_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            )
        )
        await session.commit()

    return cast(str, email)


@pytest.fixture
def jwt_encoder() -> JwtTokenEncoder:
    return JwtTokenEncoder(config=FakeConfig())


@pytest.fixture
def url_v1() -> str:
    return "/api/v1"
