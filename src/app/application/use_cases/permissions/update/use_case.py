from uuid import UUID

from src.app.application.entities.permission import PermissionEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.permissions.exceptions import (
    PermissionAlreadyExistException,
    PermissionNotFoundException,
)
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
)


class UpdatePermissionUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, dto: UpdatePermissionRequestDto, permission_id: UUID
    ) -> PermissionEntity:
        async with self._rdbms_uow():
            permission = await self._rdbms_uow.permissions.get_by_id(
                permission_id=permission_id
            )
            if permission is None:
                raise PermissionNotFoundException()

            exist = await self._rdbms_uow.permissions.get_by_name(dto.name)
            if exist and exist.id != permission_id:
                raise PermissionAlreadyExistException()

            await self._rdbms_uow.permissions.update(
                dto=dto, permission_id=permission_id
            )

            new_permission = await self._rdbms_uow.permissions.get_by_id(
                permission_id=permission_id
            )

        assert new_permission is not None
        return new_permission
