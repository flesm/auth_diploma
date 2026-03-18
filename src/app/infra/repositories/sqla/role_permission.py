from uuid import UUID

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.interfaces.repositories.rdbms.role_permission import (
    IRolePermissionRepository,
)
from src.app.infra.connection_engines.sqla.models import role_permissions


class SQLARolePermissionRepository(IRolePermissionRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def exist(self, role_id: UUID, permission_id: UUID) -> bool:
        result = await self._session.execute(
            select(role_permissions).where(
                role_permissions.c.role_id == role_id,
                role_permissions.c.permission_id == permission_id,
            )
        )

        role_permission = result.scalar()
        return True if role_permission else False

    async def attach(self, role_id: UUID, permission_id: UUID) -> None:
        await self._session.execute(
            insert(role_permissions).values(
                role_id=role_id,
                permission_id=permission_id,
            )
        )

    async def detach(self, role_id: UUID, permission_id: UUID) -> None:
        await self._session.execute(
            delete(role_permissions).where(
                role_permissions.c.role_id == role_id,
                role_permissions.c.permission_id == permission_id,
            )
        )
