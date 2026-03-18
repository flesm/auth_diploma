from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.use_cases.users.profile.get.use_case import (
    ListUsersUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


async def test_get_list_of_users_success(
    fake_uow: FakeSQLAUnitOfWork,
    get_list_of_user_uc: ListUsersUseCase,
    user_with_common_role: UserEntity,
    user_with_admin_role: UserEntity,
    user_with_superadmin_role: UserEntity,
) -> None:

    result = await get_list_of_user_uc()

    assert len(result or []) == len(fake_uow.users.users)


async def test_get_list_of_users_with_offset_success(
    fake_uow: FakeSQLAUnitOfWork,
    get_list_of_user_uc: ListUsersUseCase,
    user_with_common_role: UserEntity,
    user_with_admin_role: UserEntity,
    user_with_superadmin_role: UserEntity,
) -> None:

    result = await get_list_of_user_uc(offset=1)

    assert len(result or []) == 2


async def test_get_list_of_users_with_limit_success(
    fake_uow: FakeSQLAUnitOfWork,
    get_list_of_user_uc: ListUsersUseCase,
    user_with_common_role: UserEntity,
    user_with_admin_role: UserEntity,
    user_with_superadmin_role: UserEntity,
) -> None:

    result = await get_list_of_user_uc(limit=1)

    assert len(result or []) == 1


async def test_get_list_of_users_with_first_name_sort_success(
    fake_uow: FakeSQLAUnitOfWork,
    get_list_of_user_uc: ListUsersUseCase,
    user_with_common_role: UserEntity,
    user_with_admin_role: UserEntity,
    user_with_superadmin_role: UserEntity,
) -> None:

    result = await get_list_of_user_uc(
        sort_by=UserSortBy.FIRST_NAME, sort_desc=True
    )

    first_names = [u.first_name for u in (result or [])]

    assert first_names == sorted(first_names, reverse=True)
