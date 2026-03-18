from uuid import UUID

from sqlalchemy import asc, delete, desc, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.interfaces.repositories.rdbms.user import (
    IUserRepository,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.app.infra.connection_engines.sqla.models.user import User


class SQLAUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, user_id: UUID) -> UserEntity | None:
        result = await self._session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar()
        return user.to_entity() if user else None

    async def get_by_email(self, email: str) -> UserEntity | None:
        result = await self._session.execute(
            select(User).where(User.email == email)
        )
        user = result.scalar()
        return user.to_entity() if user else None

    async def get_users(
        self,
        offset: int = 0,
        limit: int = 10,
        sort_by: UserSortBy | None = None,
        sort_desc: bool = False,
        filter_role: str | None = None,
    ) -> list[UserEntity] | None:

        query = select(User)

        if filter_role:
            query = query.where(User.role.has(name=filter_role))

        if sort_by:
            order = desc if sort_desc else asc

            sort_columns = {
                UserSortBy.CREATED_AT: User.created_at,
                UserSortBy.ROLE: User.role,
                UserSortBy.FIRST_NAME: User.first_name,
                UserSortBy.LAST_NAME: User.last_name,
            }

            query = query.order_by(order(sort_columns[sort_by]))

        query = query.offset(offset).limit(limit)

        result = await self._session.execute(query)
        users = result.scalars().all()

        return [u.to_entity() for u in users]

    async def create(self, dto: RegisterUserRequestDTO) -> UserEntity:
        user = User(
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            hashed_password=dto.hashed_password,
            role_id=dto.role_id,
        )
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        return user.to_entity()

    async def update_password(
        self, user: UserEntity, new_hashed_password: str
    ) -> None:
        await self._session.execute(
            update(User)
            .where(User.id == user.id)
            .values(hashed_password=new_hashed_password)
        )

    async def update_profile(
        self, user: UserEntity, updated_fields: dict[str, str]
    ) -> None:
        await self._session.execute(
            update(User).where(User.id == user.id).values(**updated_fields)
        )

    async def mark_as_verified(self, user: UserEntity) -> None:
        await self._session.execute(
            update(User).where(User.id == user.id).values(is_verified=True)
        )

    async def delete_profile(self, user_id: UUID) -> None:
        await self._session.execute(delete(User).where(User.id == user_id))
