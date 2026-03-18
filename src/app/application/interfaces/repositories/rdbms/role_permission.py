from abc import ABC, abstractmethod
from uuid import UUID


class IRolePermissionRepository(ABC):

    @abstractmethod
    async def exist(self, role_id: UUID, permission_id: UUID) -> bool:
        pass

    @abstractmethod
    async def attach(self, role_id: UUID, permission_id: UUID) -> None:
        pass

    @abstractmethod
    async def detach(self, role_id: UUID, permission_id: UUID) -> None:
        pass
