from uuid import UUID, uuid4

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


class FakeSQLAPermissionRepository(IPermissionRepository):
    def __init__(self) -> None:
        self._permissions: list[PermissionEntity] = []

    async def get_by_id(self, permission_id: UUID) -> PermissionEntity | None:
        return next(
            (p for p in self._permissions if p.id == permission_id), None
        )

    async def get_by_name(
        self, permission_name: str
    ) -> PermissionEntity | None:
        return next(
            (p for p in self._permissions if p.name == permission_name), None
        )

    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[PermissionEntity]:
        start = offset or 0
        end = start + limit if limit is not None else None
        return list(self._permissions)[start:end]

    async def create(
        self, dto: CreatePermissionRequestDto
    ) -> PermissionEntity:
        permission = PermissionEntity(
            id=uuid4(),
            name=dto.name,
            description=dto.description,
        )
        self._permissions.append(permission)
        return permission

    async def update(
        self, dto: UpdatePermissionRequestDto, permission_id: UUID
    ) -> None:
        for p in self._permissions:
            if p.id == permission_id:
                p.name = dto.name
                p.description = dto.description
                break

    async def delete(self, permission_id: UUID) -> None:
        self._permissions = [
            p for p in self._permissions if p.id != permission_id
        ]

    @property
    def permissions(self) -> list[PermissionEntity]:
        return self._permissions
