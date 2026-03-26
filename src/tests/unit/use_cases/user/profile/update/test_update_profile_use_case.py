from uuid import UUID

import pytest

from src.app.application.entities.user import UserEntity
from src.app.application.use_cases.users.exceptions import UserNotFound
from src.app.application.use_cases.users.profile.update.use_case import (
    UpdateProfileUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


class TestUpdateProfileUseCase:

    async def test_case_1(
        self,
        fake_uow: FakeSQLAUnitOfWork,
        update_user_profile_uc: UpdateProfileUseCase,
        user_with_common_role: UserEntity,
        payload_for_update_common_user_profile: dict[str, str],
    ) -> None:

            result = await update_user_profile_uc(
                user_id=user_with_common_role.id,
                updated_data=payload_for_update_common_user_profile,
            )

            assert (
                result.first_name
                == payload_for_update_common_user_profile["first_name"]
            )

    async def test_case_2(
        self,
        fake_uow: FakeSQLAUnitOfWork,
        update_user_profile_uc: UpdateProfileUseCase,
        foreign_user_id: UUID,
        payload_for_update_common_user_profile: dict[str, str],
    ) -> None:

            with pytest.raises(UserNotFound):
                await update_user_profile_uc(
                    user_id=foreign_user_id,
                    updated_data=payload_for_update_common_user_profile,
                )
