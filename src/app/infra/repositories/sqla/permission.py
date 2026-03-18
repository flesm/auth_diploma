from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.entities.permission import PermissionEntity
from src.app.application.interfaces.repositories.rdbms.permission import (
    IPermissionRepository,
)
from src.app.application.use_cases.permissions.create.dto import (
    CreatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
)
from src.app.infra.connection_engines.sqla.models import Permission


class SQLAPermissionRepository(IPermissionRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, permission_id: UUID) -> PermissionEntity | None:
        result = await self._session.execute(
            select(Permission).where(Permission.id == permission_id)
        )
        permission = result.scalar()
        return permission.to_entity() if permission else None

    async def get_by_name(
        self, permission_name: str
    ) -> PermissionEntity | None:
        result = await self._session.execute(
            select(Permission).where(Permission.name == permission_name)
        )
        permission = result.scalar()
        return permission.to_entity() if permission else None

    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[PermissionEntity]:
        query = select(Permission)

        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self._session.execute(query)
        permissions = result.scalars().all()
        return [permission.to_entity() for permission in permissions]

    async def create(
        self, dto: CreatePermissionRequestDto
    ) -> PermissionEntity:

        permission = Permission(
            name=dto.name,
            description=dto.description,
        )
        self._session.add(permission)
        await self._session.commit()
        await self._session.refresh(permission)
        return permission.to_entity()

    async def update(
        self, dto: UpdatePermissionRequestDto, permission_id: UUID
    ) -> None:
        await self._session.execute(
            update(Permission)
            .where(Permission.id == permission_id)
            .values(name=dto.name, description=dto.description)
        )

    async def delete(self, permission_id: UUID) -> None:
        await self._session.execute(
            delete(Permission).where(Permission.id == permission_id)
        )
