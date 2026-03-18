from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.permissions.create.use_case import (
    CreatePermissionUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.permission.create.view_models import (
    CreatePermissionRequestViewModel,
    CreatePermissionResponseViewModel,
)

router = APIRouter()


@router.post("", response_model=CreatePermissionResponseViewModel)
@inject
async def create_permission(
    view_model: CreatePermissionRequestViewModel,
    create_permission_uc: CreatePermissionUseCase = Depends(
        Provide[Container.create_permission]
    ),
) -> CreatePermissionResponseViewModel:
    dto = view_model.to_dto()

    permission = await create_permission_uc(dto=dto)

    return CreatePermissionResponseViewModel.from_entity(entity=permission)
