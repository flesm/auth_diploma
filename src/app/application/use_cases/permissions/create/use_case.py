from src.app.application.entities.permission import PermissionEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.permissions.create.dto import (
    CreatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.exceptions import (
    PermissionAlreadyExistException,
)


class CreatePermissionUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork) -> None:
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, dto: CreatePermissionRequestDto
    ) -> PermissionEntity:
        async with self._rdbms_uow():
            existing = await self._rdbms_uow.permissions.get_by_name(
                permission_name=dto.name
            )
            if existing:
                raise PermissionAlreadyExistException()

            permission = await self._rdbms_uow.permissions.create(dto=dto)

        return permission
