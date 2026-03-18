from uuid import UUID, uuid4

import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.infra.connection_engines.sqla.models import User


@pytest.fixture
def url_profile(url_v1: str) -> str:
    return f"{url_v1}/profile"


@pytest_asyncio.fixture
async def common_user_id(
    async_session: async_sessionmaker, faker: Faker
) -> UUID:

    user_id = uuid4()

    async with async_session() as session:
        await session.execute(
            insert(User).values(
                id=user_id,
                email=faker.email(),
                hashed_password=faker.password(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                is_verified=True,
                is_active=True,
                role_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            )
        )
        await session.commit()

    return user_id
