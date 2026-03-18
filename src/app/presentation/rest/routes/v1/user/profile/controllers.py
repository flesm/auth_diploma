from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.entities.user import UserEntity
from src.app.application.enums.user_sort_by import UserSortBy
from src.app.application.use_cases.users.profile.delete.use_case import (
    DeleteProfileUseCase,
)
from src.app.application.use_cases.users.profile.get.use_case import (
    ListUsersUseCase,
)
from src.app.application.use_cases.users.profile.update.use_case import (
    UpdateProfileUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.get("")
@inject
async def get_list_of_users(
    offset: int = 0,
    limit: int = 10,
    sort_by: UserSortBy = UserSortBy.CREATED_AT,
    sort_desc: bool = False,
    filter_role: str | None = None,
    get_list_of_users_uc: ListUsersUseCase = Depends(
        Provide[Container.get_list_of_users]
    ),
) -> list[UserEntity] | None:

    return await get_list_of_users_uc(
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_desc=sort_desc,
        filter_role=filter_role,
    )


@router.patch("")
@inject
async def update_users_profile(
    user_id: UUID,
    updated_data: dict[str, str],
    update_profile_uc: UpdateProfileUseCase = Depends(
        Provide[Container.update_profile]
    ),
) -> UserEntity:

    return await update_profile_uc(user_id=user_id, updated_data=updated_data)


@router.delete("")
@inject
async def delete_users_profile(
    user_id: UUID,
    delete_profile_uc: DeleteProfileUseCase = Depends(
        Provide[Container.delete_profile]
    ),
) -> None:

    await delete_profile_uc(user_id=user_id)
