from uuid import UUID

from src.app.application.entities.user import UserEntity
from src.app.application.interfaces.unit_of_work.rdbms_uow import IUnitOfWork
from src.app.application.use_cases.users.exceptions import UserNotFound


class UpdateProfileUseCase:
    def __init__(self, rdbms_uow: IUnitOfWork):
        self._rdbms_uow = rdbms_uow

    async def __call__(
        self, user_id: UUID, updated_data: dict[str, str]
    ) -> UserEntity:
        async with self._rdbms_uow():
            user = await self._rdbms_uow.users.get_by_id(user_id=user_id)
            if not user:
                raise UserNotFound()

            for field, value in updated_data.items():
                setattr(user, field, value)

            await self._rdbms_uow.users.update_profile(
                user=user, updated_fields=updated_data
            )

        return user
