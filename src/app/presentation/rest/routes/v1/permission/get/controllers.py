from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.entities.permission import PermissionEntity
from src.app.application.use_cases.permissions.get.use_case import (
    GetAllPermissionsUseCase,
    GetPermissionByIdUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.get("/{permission_id}")
@inject
async def get_permission_by_id(
    permission_id: UUID,
    get_permission_by_id_uc: GetPermissionByIdUseCase = Depends(
        Provide[Container.get_permission_by_id]
    ),
) -> PermissionEntity:

    return await get_permission_by_id_uc(permission_id=permission_id)


@router.get("")
@inject
async def get_all_permissions(
    offset: int | None = None,
    limit: int | None = None,
    get_all_permissions_uc: GetAllPermissionsUseCase = Depends(
        Provide[Container.get_all_permissions]
    ),
) -> list[PermissionEntity] | None:
    return await get_all_permissions_uc(offset=offset, limit=limit)
