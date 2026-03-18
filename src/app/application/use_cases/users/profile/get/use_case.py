from typing import List

from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork


class ListUsersUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self,
        offset: int = 0,
        limit: int = 10,
        sort_by: UserSortBy = UserSortBy.CREATED_AT,
        sort_desc: bool = False,
        filter_role: str | None = None,
    ) -> List[UserEntity] | None:
        async with self._rdbms_uow():
            users = await self._rdbms_uow.users.get_users(
                offset=offset,
                limit=limit,
                sort_by=sort_by,
                sort_desc=sort_desc,
                filter_role=filter_role,
            )
        return users
