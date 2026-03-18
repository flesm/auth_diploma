from abc import ABC, abstractmethod
from typing import Any, Self

from src.app.application.interfaces.repositories.rdbms.permission import (
    IPermissionRepository,
)
from src.app.application.interfaces.repositories.rdbms.role import (
    IRoleRepository,
)
from src.app.application.interfaces.repositories.rdbms.role_permission import (
    IRolePermissionRepository,
)
from src.app.application.interfaces.repositories.rdbms.user import (
    IUserRepository,
)


class IUnitOfWork(ABC):

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        return self

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, *args: Any, **kwargs: Any
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

        await self.shutdown()

    @property
    @abstractmethod
    def users(self) -> IUserRepository: ...

    @property
    @abstractmethod
    def roles(self) -> IRoleRepository:
        pass

    @property
    @abstractmethod
    def permissions(self) -> IPermissionRepository:
        pass

    @property
    @abstractmethod
    def roles_permissions(self) -> IRolePermissionRepository:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    @abstractmethod
    async def shutdown(self) -> None:
        pass
