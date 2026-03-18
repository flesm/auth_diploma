from abc import ABC, abstractmethod
from uuid import UUID

from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)


class IUserRepository(ABC):

    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> UserEntity | None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> UserEntity | None:
        pass

    @abstractmethod
    async def get_users(
        self,
        offset: int = 0,
        limit: int = 10,
        sort_by: UserSortBy | None = None,
        sort_desc: bool = False,
        filter_role: str | None = None,
    ) -> list[UserEntity] | None:
        pass

    @abstractmethod
    async def create(self, dto: RegisterUserRequestDTO) -> UserEntity:
        pass

    @abstractmethod
    async def update_password(
        self, user: UserEntity, new_hashed_password: str
    ) -> None:
        pass

    @abstractmethod
    async def update_profile(
        self, user: UserEntity, updated_fields: dict[str, str]
    ) -> None:
        pass

    @abstractmethod
    async def mark_as_verified(self, user: UserEntity) -> None:
        pass

    @abstractmethod
    async def delete_profile(self, user_id: UUID) -> None:
        pass
