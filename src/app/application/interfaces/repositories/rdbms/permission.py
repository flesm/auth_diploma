from abc import ABC, abstractmethod
from uuid import UUID

from src.app.application.entities.permission import PermissionEntity
from src.app.application.use_cases.permissions.create.dto import (
    CreatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
)


class IPermissionRepository(ABC):

    @abstractmethod
    async def get_by_id(self, permission_id: UUID) -> PermissionEntity | None:
        pass

    @abstractmethod
    async def get_by_name(
        self, permission_name: str
    ) -> PermissionEntity | None:
        pass

    @abstractmethod
    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[PermissionEntity]:
        pass

    @abstractmethod
    async def create(
        self, dto: CreatePermissionRequestDto
    ) -> PermissionEntity:
        pass

    @abstractmethod
    async def update(
        self, dto: UpdatePermissionRequestDto, permission_id: UUID
    ) -> None:
        pass

    @abstractmethod
    async def delete(self, permission_id: UUID) -> None:
        pass
