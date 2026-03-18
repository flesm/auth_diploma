from typing import cast
from uuid import uuid4

import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.infra.connection_engines.sqla.models import Permission


@pytest.fixture
def url_permission(url_v1: str) -> str:
    return f"{url_v1}/permission"


@pytest_asyncio.fixture
async def regular_permission_id(
    async_session: async_sessionmaker, faker: Faker
) -> str:

    permission_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(Permission).values(
                id=permission_id,
                name=faker.name(),
                description=faker.random_letter(),
            )
        )
        await session.commit()

    return cast(str, permission_id)
