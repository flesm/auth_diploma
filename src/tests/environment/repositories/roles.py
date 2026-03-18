from uuid import UUID, uuid4

from src.app.application.entities.role import RoleEntity
from src.app.application.interfaces.repositories.rdbms.role import (
    IRoleRepository,
)
from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto


class FakeSQLARoleRepository(IRoleRepository):
    def __init__(self) -> None:
        self._roles: list[RoleEntity] = []

    async def get_by_id(self, role_id: UUID) -> RoleEntity | None:
        return next((r for r in self._roles if r.id == role_id), None)

    async def get_by_name(self, role_name: str) -> RoleEntity | None:
        return next((r for r in self._roles if r.name == role_name), None)

    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[RoleEntity]:
        start = offset or 0
        end = start + limit if limit is not None else None
        return list(self._roles)[start:end]

    async def create(self, dto: CreateRoleRequestDto) -> RoleEntity:
        role = RoleEntity(
            id=uuid4(),
            name=dto.name,
            description=dto.description,
        )
        self._roles.append(role)
        return role

    async def update(self, dto: UpdateRoleRequestDto, role_id: UUID) -> None:
        for r in self._roles:
            if r.id == role_id:
                r.name = dto.name
                r.description = dto.description
                break

    async def delete(self, role_id: UUID) -> None:
        self._roles = [r for r in self._roles if r.id != role_id]

    @property
    def roles(self) -> list[RoleEntity]:
        return self._roles
