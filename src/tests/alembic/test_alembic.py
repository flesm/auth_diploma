import os
from typing import Any, AsyncGenerator

import pytest
import pytest_asyncio
from alembic.config import Config
from pytest_alembic.tests import (  # noqa
    test_model_definitions_match_ddl,
    test_single_head_revision,
    test_up_down_consistency,
    test_upgrade,
)
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    create_async_engine,
)

from src.tests.environment.config import FakeConfig


@pytest_asyncio.fixture(scope="module")
async def sqla_engine(
    fake_config: FakeConfig,
) -> AsyncGenerator[AsyncEngine, Any]:
    engine = create_async_engine(str(fake_config.DB.dsn), echo=True)
    try:
        yield engine
    finally:
        await engine.dispose()


@pytest.fixture(scope="module")
def alembic_config() -> Config:
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )
    alembic_path = os.path.join(base_dir, "alembic.ini")
    return Config(alembic_path)


@pytest.fixture(scope="module")
async def alembic_engine(
    sqla_engine: AsyncEngine,
) -> AsyncGenerator[AsyncConnection, Any]:
    async with sqla_engine.connect() as connection:
        yield connection
