from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.roles.update.use_case import (
    UpdateRoleUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.role.update.view_models import (
    UpdateRoleRequestViewModel,
    UpdateRoleResponseViewModel,
)

router = APIRouter()


@router.patch("", response_model=UpdateRoleResponseViewModel)
@inject
async def update_role(
    role_id: UUID,
    view_model: UpdateRoleRequestViewModel,
    update_role_uc: UpdateRoleUseCase = Depends(
        Provide[Container.update_role]
    ),
) -> UpdateRoleResponseViewModel:
    dto = view_model.to_dto()

    new_role = await update_role_uc(dto=dto, role_id=role_id)

    return UpdateRoleResponseViewModel.from_entity(entity=new_role)
