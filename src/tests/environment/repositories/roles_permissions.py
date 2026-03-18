from uuid import UUID

from src.app.application.interfaces.repositories.rdbms.role_permission import (
    IRolePermissionRepository,
)


class FakeSQLARolePermissionRepository(IRolePermissionRepository):
    def __init__(self) -> None:
        self._role_permissions: set[tuple[UUID, UUID]] = set()

    async def exist(self, role_id: UUID, permission_id: UUID) -> bool:
        return (role_id, permission_id) in self._role_permissions

    async def attach(self, role_id: UUID, permission_id: UUID) -> None:
        self._role_permissions.add((role_id, permission_id))

    async def detach(self, role_id: UUID, permission_id: UUID) -> None:
        self._role_permissions.discard((role_id, permission_id))

    @property
    def role_permissions(self) -> set[tuple[UUID, UUID]]:
        return self._role_permissions
