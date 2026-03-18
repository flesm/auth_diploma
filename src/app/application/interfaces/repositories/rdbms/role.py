from abc import ABC, abstractmethod
from uuid import UUID

from src.app.application.entities.role import RoleEntity
from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto


class IRoleRepository(ABC):

    @abstractmethod
    async def get_by_id(self, role_id: UUID) -> RoleEntity | None:
        pass

    @abstractmethod
    async def get_by_name(self, role_name: str) -> RoleEntity | None:
        pass

    @abstractmethod
    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[RoleEntity]:
        pass

    @abstractmethod
    async def create(self, dto: CreateRoleRequestDto) -> RoleEntity:
        pass

    @abstractmethod
    async def update(self, dto: UpdateRoleRequestDto, role_id: UUID) -> None:
        pass

    @abstractmethod
    async def delete(self, role_id: UUID) -> None:
        pass
