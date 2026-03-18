from uuid import UUID

from src.app.application.entities.role import RoleEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.roles.exceptions import (
    RoleAlreadyExistException,
    RoleNotFoundException,
)
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto


class UpdateRoleUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, dto: UpdateRoleRequestDto, role_id: UUID
    ) -> RoleEntity:
        async with self._rdbms_uow():
            role = await self._rdbms_uow.roles.get_by_id(role_id=role_id)
            if role is None:
                raise RoleNotFoundException()

            exist = await self._rdbms_uow.roles.get_by_name(dto.name)
            if exist and exist.id != role_id:
                raise RoleAlreadyExistException()

            await self._rdbms_uow.roles.update(dto=dto, role_id=role_id)

            new_role = await self._rdbms_uow.roles.get_by_id(role_id=role_id)

        assert new_role is not None
        return new_role
