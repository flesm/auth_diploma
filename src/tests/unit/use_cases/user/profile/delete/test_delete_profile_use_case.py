from uuid import UUID

import pytest

from src.app.application.entities.user import UserEntity
from src.app.application.use_cases.users.exceptions import UserNotFound
from src.app.application.use_cases.users.profile.delete.use_case import (
    DeleteProfileUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_delete_common_user_profile_success(
    fake_uow: FakeSQLAUnitOfWork,
    delete_user_profile_uc: DeleteProfileUseCase,
    user_with_common_role: UserEntity,
) -> None:

    assert len(fake_uow.users.users) == 1
    await delete_user_profile_uc(user_id=user_with_common_role.id)
    assert len(fake_uow.users.users) == 0


async def test_delete_foreign_user_profile_not_found(
    fake_uow: FakeSQLAUnitOfWork,
    delete_user_profile_uc: DeleteProfileUseCase,
    foreign_user_id: UUID,
) -> None:
    with pytest.raises(UserNotFound):
        await delete_user_profile_uc(user_id=foreign_user_id)
