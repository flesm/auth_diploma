from uuid import UUID

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)


class AttachPermissionToRoleUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork) -> None:
        self._rdbms_uow = rdbms_uow

    async def __call__(self, role_id: UUID, permission_id: UUID) -> None:
        async with self._rdbms_uow():
            role = await self._rdbms_uow.roles.get_by_id(role_id)
            if not role:
                raise RoleNotFoundException()

            permission = await self._rdbms_uow.permissions.get_by_id(
                permission_id
            )
            if not permission:
                raise PermissionNotFoundException()

            exists = await self._rdbms_uow.roles_permissions.exist(
                role_id=role_id,
                permission_id=permission_id,
            )
            if not exists:
                await self._rdbms_uow.roles_permissions.attach(
                    role_id=role_id,
                    permission_id=permission_id,
                )
