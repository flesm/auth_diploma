from uuid import UUID

from src.app.application.entities.role import RoleEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)


class GetRoleByIdUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(self, role_id: UUID) -> RoleEntity:
        async with self._rdbms_uow():
            role = await self._rdbms_uow.roles.get_by_id(role_id=role_id)

        if role is None:
            raise RoleNotFoundException()
        return role


class GetAllRolesUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, offset: int | None = None, limit: int | None = None
    ) -> list[RoleEntity]:
        async with self._rdbms_uow():
            return await self._rdbms_uow.roles.get_all(
                offset=offset, limit=limit
            )
