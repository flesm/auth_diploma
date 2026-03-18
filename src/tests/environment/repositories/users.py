from datetime import datetime
from uuid import UUID, uuid4

from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.interfaces.repositories.rdbms.user import (
    IUserRepository,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)


class FakeSQLAUsersRepository(IUserRepository):
    def __init__(self) -> None:
        self._users: list[UserEntity] = []

    async def get_by_id(self, user_id: UUID) -> UserEntity | None:
        return next((u for u in self._users if u.id == user_id), None)

    async def get_by_email(self, email: str) -> UserEntity | None:
        return next((u for u in self._users if u.email == email), None)

    async def get_users(
        self,
        offset: int = 0,
        limit: int = 10,
        sort_by: UserSortBy | None = None,
        sort_desc: bool = False,
        filter_role: str | None = None,
    ) -> list[UserEntity] | None:
        users = self._users.copy()

        if filter_role:
            users = [u for u in users if str(u.role_id) == filter_role]

        if sort_by:
            reverse = sort_desc
            sort_keys = {
                UserSortBy.CREATED_AT: lambda u: u.created_at,
                UserSortBy.FIRST_NAME: lambda u: u.first_name,
                UserSortBy.LAST_NAME: lambda u: u.last_name,
                UserSortBy.ROLE: lambda u: str(u.role_id),
            }
            users.sort(key=sort_keys[sort_by], reverse=reverse)

        start = offset
        end = offset + limit
        return users[start:end]

    async def create(self, dto: RegisterUserRequestDTO) -> UserEntity:
        user = UserEntity(
            id=uuid4(),
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            hashed_password=dto.hashed_password,
            role_id=dto.role_id,
            is_verified=False,
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self._users.append(user)
        return user

    async def update_password(
        self, user: UserEntity, new_hashed_password: str
    ) -> None:
        for u in self._users:
            if u.id == user.id:
                u.hashed_password = new_hashed_password
                break

    async def update_profile(
        self, user: UserEntity, updated_fields: dict[str, str]
    ) -> None:
        for u in self._users:
            if u.id == user.id:
                for field, value in updated_fields.items():
                    setattr(u, field, value)
                u.updated_at = datetime.now()
                break

    async def mark_as_verified(self, user: UserEntity) -> None:
        for u in self._users:
            if u.id == user.id:
                u.is_verified = True
                break

    async def delete_profile(self, user_id: UUID) -> None:
        self._users = [u for u in self._users if u.id != user_id]

    @property
    def users(self) -> list[UserEntity]:
        return self._users
