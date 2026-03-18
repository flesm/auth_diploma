from src.app.application.entities.role import RoleEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.exceptions import (
    RoleAlreadyExistException,
)


class CreateRoleUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork) -> None:
        self._rdbms_uow = rdbms_uow

    async def __call__(self, dto: CreateRoleRequestDto) -> RoleEntity:
        async with self._rdbms_uow():
            existing = await self._rdbms_uow.roles.get_by_name(
                role_name=dto.name
            )
            if existing:
                raise RoleAlreadyExistException()

            role = await self._rdbms_uow.roles.create(dto=dto)

        return role
