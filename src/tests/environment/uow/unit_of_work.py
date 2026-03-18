from typing import Self

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.tests.environment.repositories.permissions import (
    FakeSQLAPermissionRepository,
)
from src.tests.environment.repositories.roles import FakeSQLARoleRepository
from src.tests.environment.repositories.roles_permissions import (
    FakeSQLARolePermissionRepository,
)
from src.tests.environment.repositories.users import FakeSQLAUsersRepository


class FakeSQLAUnitOfWork(IUnitOfWork):
    def __init__(self) -> None:
        self._users = FakeSQLAUsersRepository()
        self._roles = FakeSQLARoleRepository()
        self._permissions = FakeSQLAPermissionRepository()
        self._roles_permissions = FakeSQLARolePermissionRepository()

    @property
    def users(self) -> FakeSQLAUsersRepository:
        return self._users

    @property
    def roles(self) -> FakeSQLARoleRepository:
        return self._roles

    @property
    def permissions(self) -> FakeSQLAPermissionRepository:
        return self._permissions

    @property
    def roles_permissions(self) -> FakeSQLARolePermissionRepository:
        return self._roles_permissions

    async def __aenter__(self) -> Self:
        return self

    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass
