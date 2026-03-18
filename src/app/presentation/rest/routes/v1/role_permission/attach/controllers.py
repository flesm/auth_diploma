from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.roles_permissions.attach.use_case import (
    AttachPermissionToRoleUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.post("/role/{role_id}/permission/{permission_id}")
@inject
async def attach_permission_to_role(
    role_id: UUID,
    permission_id: UUID,
    attach_permission_to_role_uc: AttachPermissionToRoleUseCase = Depends(
        Provide[Container.attach_permission_to_role]
    ),
) -> None:

    return await attach_permission_to_role_uc(
        role_id=role_id, permission_id=permission_id
    )
