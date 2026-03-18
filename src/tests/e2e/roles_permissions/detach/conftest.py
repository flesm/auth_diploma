import pytest
import pytest_asyncio
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.infra.connection_engines.sqla.models import role_permissions


@pytest.fixture
def url_role_permission_detach(url_role_permission: str) -> str:
    return (
        f"{url_role_permission}/role/{{role_id}}/permission/{{permission_id}}"
    )


@pytest_asyncio.fixture
async def attached_permission_ro_role(
    async_session: async_sessionmaker,
    another_regular_role_id: str,
    another_regular_permission_id: str,
) -> None:
    async with async_session() as session:
        await session.execute(
            insert(role_permissions).values(
                role_id=another_regular_role_id,
                permission_id=another_regular_permission_id,
            )
        )
        await session.commit()
