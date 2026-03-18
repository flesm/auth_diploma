from uuid import uuid4

import pytest
import pytest_asyncio
from faker import Faker
from passlib.context import CryptContext
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.infra.connection_engines.sqla.models import User


@pytest.fixture
def crypto() -> CryptContext:
    return CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture
def url_login_user(url_auth: str) -> str:
    return f"{url_auth}/login"


@pytest_asyncio.fixture
async def login_payload_of_regular_user(
    async_session: async_sessionmaker, faker: Faker, crypto: CryptContext
) -> dict[str, str]:
    email = faker.unique.email()
    password = faker.password()

    hashed_password = crypto.hash(password)

    async with async_session() as session:
        await session.execute(
            insert(User).values(
                id=uuid4(),
                email=email,
                hashed_password=hashed_password,
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                is_verified=False,
                is_active=True,
                role_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            )
        )
        await session.commit()

    return {"email": email, "password": password}


@pytest.fixture
def login_payload_of_foreign_user(faker: Faker) -> dict[str, str]:
    return {"email": faker.email(), "password": faker.password()}
