from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.entities.role import RoleEntity
from src.app.application.interfaces.repositories.rdbms.role import (
    IRoleRepository,
)
from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto
from src.app.infra.connection_engines.sqla.models import Role


class SQLARoleRepository(IRoleRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, role_id: UUID) -> RoleEntity | None:
        result = await self._session.execute(
            select(Role).where(Role.id == role_id)
        )
        role = result.scalar()
        return role.to_entity() if role else None

    async def get_by_name(self, role_name: str) -> RoleEntity | None:
        result = await self._session.execute(
            select(Role).where(Role.name == role_name)
        )
        role = result.scalar()
        return role.to_entity() if role else None

    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[RoleEntity]:
        query = select(Role)

        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self._session.execute(query)
        roles = result.scalars().all()
        return [role.to_entity() for role in roles]

    async def create(self, dto: CreateRoleRequestDto) -> RoleEntity:
        role = Role(name=dto.name, description=dto.description)
        self._session.add(role)
        await self._session.commit()
        await self._session.refresh(role)
        return role.to_entity()

    async def update(self, dto: UpdateRoleRequestDto, role_id: UUID) -> None:
        await self._session.execute(
            update(Role)
            .where(Role.id == role_id)
            .values(name=dto.name, description=dto.description)
        )

    async def delete(self, role_id: UUID) -> None:
        await self._session.execute(delete(Role).where(Role.id == role_id))
