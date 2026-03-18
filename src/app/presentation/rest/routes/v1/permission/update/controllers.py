from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.permissions.update.use_case import (
    UpdatePermissionUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.permission.update.view_models import (
    UpdatePermissionRequestViewModel,
    UpdatePermissionResponseViewModel,
)

router = APIRouter()


@router.patch("", response_model=UpdatePermissionResponseViewModel)
@inject
async def update_permission(
    permission_id: UUID,
    view_model: UpdatePermissionRequestViewModel,
    update_permission_uc: UpdatePermissionUseCase = Depends(
        Provide[Container.update_permission]
    ),
) -> UpdatePermissionResponseViewModel:
    dto = view_model.to_dto()

    new_permission = await update_permission_uc(
        dto=dto, permission_id=permission_id
    )

    return UpdatePermissionResponseViewModel.from_entity(entity=new_permission)
