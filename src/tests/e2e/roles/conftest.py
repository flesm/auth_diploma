from typing import cast
from uuid import uuid4

import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.infra.connection_engines.sqla.models import (
    Permission,
    Role,
    role_permissions,
)


@pytest.fixture
def url_role(url_v1: str) -> str:
    return f"{url_v1}/role"


@pytest_asyncio.fixture
async def regular_role_id(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    role_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(Role).values(
                id=role_id,
                name=faker.name(),
                description=faker.random_letter(),
            )
        )
        await session.commit()

    return cast(str, role_id)


@pytest_asyncio.fixture
async def role_with_permission_id(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    role_id = uuid4()
    permission_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(Role).values(
                id=role_id,
                name=faker.name(),
                description=faker.random_letter(),
            )
        )
        await session.execute(
            insert(Permission).values(
                id=permission_id,
                name="role:test",
                description=faker.random_letter(),
            )
        )
        await session.execute(
            insert(role_permissions).values(
                role_id=role_id,
                permission_id=permission_id,
            )
        )
        await session.commit()

    return cast(str, role_id)
