from uuid import UUID

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)


class DeletePermissionUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(self, permission_id: UUID) -> str:
        async with self._rdbms_uow():
            permission = await self._rdbms_uow.permissions.get_by_id(
                permission_id=permission_id
            )
            if permission is None:
                raise PermissionNotFoundException()

            await self._rdbms_uow.permissions.delete(
                permission_id=permission_id
            )
        return permission.name
