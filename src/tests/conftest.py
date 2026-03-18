from pathlib import Path
from typing import AsyncGenerator
from uuid import UUID, uuid4

import asyncpg
import pytest
import pytest_asyncio
from alembic import command
from alembic.config import Config as AlembicConfig
from faker import Faker
from pydantic import SecretStr

from src.tests.environment.config import FakeConfig
from src.tests.environment.crypto.password_cryptografer import (
    FakePasswordCryptografer,
)
from src.tests.environment.email.email_sender import FakeFMEmailSender
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


@pytest.fixture
def faker() -> Faker:
    return Faker()


@pytest.fixture(scope="session")
def fake_config() -> FakeConfig:
    return FakeConfig()


@pytest_asyncio.fixture(scope="session")
async def pg_connection(
    fake_config: FakeConfig,
) -> AsyncGenerator[asyncpg.Connection, None]:
    db_user = fake_config.DB.user
    db_password = (
        fake_config.DB.password.get_secret_value()
        if isinstance(fake_config.DB.password, SecretStr)
        else fake_config.DB.password
    )
    db_host = fake_config.DB.host
    db_port = fake_config.DB.port

    conn = await asyncpg.connect(
        user=db_user,
        password=db_password,
        database="postgres",
        host=db_host,
        port=db_port,
    )
    try:
        yield conn
    finally:
        await conn.close()


@pytest_asyncio.fixture(scope="session")
async def create_test_database(
    pg_connection: asyncpg.Connection, fake_config: FakeConfig
) -> None:
    db_name = fake_config.DB.db
    row = await pg_connection.fetchrow(
        "SELECT 1 FROM pg_database WHERE datname = $1", db_name
    )
    if row is None:
        await pg_connection.execute(f'CREATE DATABASE "{db_name}"')


@pytest_asyncio.fixture(scope="session")
async def connection(
    fake_config: FakeConfig,
) -> AsyncGenerator[asyncpg.Connection, None]:
    db_user = fake_config.DB.user
    db_password = (
        fake_config.DB.password.get_secret_value()
        if isinstance(fake_config.DB.password, SecretStr)
        else fake_config.DB.password
    )
    db_host = fake_config.DB.host
    db_port = fake_config.DB.port
    db_name = fake_config.DB.db

    conn = await asyncpg.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host=db_host,
        port=db_port,
    )

    try:
        yield conn
    finally:
        await conn.close()


@pytest.fixture(scope="session")
def apply_migrations(
    create_test_database: None, fake_config: FakeConfig
) -> None:
    project_root = Path(__file__).parent.parent.parent
    alembic_ini_path = project_root / "alembic.ini"
    migrations_path = project_root / "src" / "app" / "infra" / "alembic"

    alembic_cfg = AlembicConfig(str(alembic_ini_path))
    alembic_cfg.set_main_option("script_location", str(migrations_path))
    alembic_cfg.set_main_option("sqlalchemy.url", str(fake_config.DB.dsn))

    command.upgrade(alembic_cfg, "head")


@pytest_asyncio.fixture(scope="session", autouse=True)
async def insert_default_roles(
    apply_migrations: None,
    connection: asyncpg.Connection,
) -> None:
    await connection.execute(
        """
        INSERT INTO roles (id, name, description) VALUES
            ('3fa85f64-5717-4562-b3fc-2c963f66afa6',
             'common',
             'common user'),
            ('5fa85f64-5717-4562-b3fc-2c963f66afa6',
             'admin',
             'admin can do anything'),
            ('8fa85f64-5717-4562-b3fc-2c963f66afa6',
             'superadmin',
             'can create other admins')
        ON CONFLICT (id) DO NOTHING;
    """
    )


@pytest.fixture
def fake_email_sender() -> FakeFMEmailSender:
    return FakeFMEmailSender()


@pytest.fixture
def fake_jwt_encoder(fake_config: FakeConfig) -> FakeJwtTokenEncoder:
    return FakeJwtTokenEncoder(config=fake_config)


@pytest.fixture
def fake_password_cryptografer() -> FakePasswordCryptografer:
    return FakePasswordCryptografer()


@pytest.fixture
def invalid_token() -> str:
    return "invalid token"


@pytest.fixture
def foreign_user_id() -> UUID:
    return uuid4()
