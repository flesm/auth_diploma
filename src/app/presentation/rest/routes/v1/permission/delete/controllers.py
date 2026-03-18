from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.permissions.delete.use_case import (
    DeletePermissionUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.delete("")
@inject
async def delete_permission(
    permission_id: UUID,
    delete_permission_uc: DeletePermissionUseCase = Depends(
        Provide[Container.delete_permission]
    ),
) -> str:
    return await delete_permission_uc(permission_id=permission_id)
