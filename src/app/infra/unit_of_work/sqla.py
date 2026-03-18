from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.infra.repositories.sqla.permission import SQLAPermissionRepository
from src.app.infra.repositories.sqla.role import SQLARoleRepository
from src.app.infra.repositories.sqla.role_permission import (
    SQLARolePermissionRepository,
)
from src.app.infra.repositories.sqla.user import SQLAUserRepository


class SQLAUnitOfWork(IUnitOfWork):

    def __init__(
        self, session_factory: async_sessionmaker[AsyncSession]
    ) -> None:
        self._session_factory = session_factory
        self._session: AsyncSession
        self._users: SQLAUserRepository | None = None
        self._roles: SQLARoleRepository | None = None
        self._permissions: SQLAPermissionRepository | None = None
        self._roles_permissions: SQLARolePermissionRepository | None = None

    async def __aenter__(self) -> Self:
        self._session = self._session_factory()

        return await super().__aenter__()

    @property
    def users(self) -> SQLAUserRepository:
        self._users = SQLAUserRepository(session=self._session)
        return self._users

    @property
    def roles(self) -> SQLARoleRepository:
        self._roles = SQLARoleRepository(session=self._session)
        return self._roles

    @property
    def permissions(self) -> SQLAPermissionRepository:
        self._permissions = SQLAPermissionRepository(session=self._session)
        return self._permissions

    @property
    def roles_permissions(self) -> SQLARolePermissionRepository:
        self._roles_permissions = SQLARolePermissionRepository(
            session=self._session
        )
        return self._roles_permissions

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def shutdown(self) -> None:
        await self._session.close()
