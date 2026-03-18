from uuid import UUID

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)


class DeleteRoleUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(self, role_id: UUID) -> str:
        async with self._rdbms_uow():
            role = await self._rdbms_uow.roles.get_by_id(role_id=role_id)
            if role is None:
                raise RoleNotFoundException()

            await self._rdbms_uow.roles.delete(role_id=role_id)

        return role.name
