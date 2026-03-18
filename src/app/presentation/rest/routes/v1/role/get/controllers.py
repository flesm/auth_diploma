from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.entities.role import RoleEntity
from src.app.application.use_cases.roles.get.controllers import (
    GetAllRolesUseCase,
    GetRoleByIdUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.get("/{role_id}")
@inject
async def get_role_by_id(
    role_id: UUID,
    get_role_by_id_uc: GetRoleByIdUseCase = Depends(
        Provide[Container.get_role_by_id]
    ),
) -> RoleEntity:

    return await get_role_by_id_uc(role_id=role_id)


@router.get("")
@inject
async def get_all_roles(
    offset: int | None = None,
    limit: int | None = None,
    get_all_roles_uc: GetAllRolesUseCase = Depends(
        Provide[Container.get_all_roles]
    ),
) -> list[RoleEntity] | None:
    return await get_all_roles_uc(offset=offset, limit=limit)
