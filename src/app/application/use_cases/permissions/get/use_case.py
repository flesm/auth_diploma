from uuid import UUID

from src.app.application.entities.permission import PermissionEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)


class GetPermissionByIdUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(self, permission_id: UUID) -> PermissionEntity:
        async with self._rdbms_uow():
            permission = await self._rdbms_uow.permissions.get_by_id(
                permission_id=permission_id
            )

        if permission is None:
            raise PermissionNotFoundException()
        return permission


class GetAllPermissionsUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, offset: int | None = None, limit: int | None = None
    ) -> list[PermissionEntity]:
        async with self._rdbms_uow():
            return await self._rdbms_uow.permissions.get_all(
                offset=offset, limit=limit
            )
