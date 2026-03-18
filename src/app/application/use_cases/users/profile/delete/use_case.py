from uuid import UUID

from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import UserNotFound


class DeleteProfileUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(self, user_id: UUID) -> None:
        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_id(user_id)
            if not user:
                raise UserNotFound()

            await self._rdbms_uow.users.delete_profile(user_id=user_id)
