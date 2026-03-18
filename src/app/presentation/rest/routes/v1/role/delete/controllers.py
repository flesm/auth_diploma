from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.roles.delete.controllers import (
    DeleteRoleUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.delete("")
@inject
async def delete_role(
    role_id: UUID,
    delete_role_uc: DeleteRoleUseCase = Depends(
        Provide[Container.delete_role]
    ),
) -> str:
    return await delete_role_uc(role_id=role_id)
