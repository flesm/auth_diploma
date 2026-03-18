from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.roles.create.use_case import (
    CreateRoleUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.role.create.view_models import (
    CreateRoleRequestViewModel,
    CreateRoleResponseViewModel,
)

router = APIRouter()


@router.post("", response_model=CreateRoleResponseViewModel)
@inject
async def create_role(
    view_model: CreateRoleRequestViewModel,
    create_role_uc: CreateRoleUseCase = Depends(
        Provide[Container.create_role]
    ),
) -> CreateRoleResponseViewModel:
    dto = view_model.to_dto()

    role = await create_role_uc(dto=dto)

    return CreateRoleResponseViewModel.from_entity(entity=role)
