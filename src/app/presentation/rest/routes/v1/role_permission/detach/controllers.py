from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.roles_permissions.detach.use_case import (
    DetachRoleWithPermissionUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.delete("/role/{role_id}/permission/{permission_id}")
@inject
async def detach_role_with_permission(
    role_id: UUID,
    permission_id: UUID,
    detach_role_with_permission_uc: DetachRoleWithPermissionUseCase = Depends(
        Provide[Container.detach_role_with_permission]
    ),
) -> None:
    return await detach_role_with_permission_uc(
        role_id=role_id, permission_id=permission_id
    )
