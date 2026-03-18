from fastapi import APIRouter

from src.app.presentation.rest.routes.v1.permission.create.controllers import (
    router as create_permission_router,
)
from src.app.presentation.rest.routes.v1.permission.delete.controllers import (
    router as delete_permission_router,
)
from src.app.presentation.rest.routes.v1.permission.get.controllers import (
    router as get_permission_router,
)
from src.app.presentation.rest.routes.v1.permission.update.controllers import (
    router as update_permission_router,
)

permission_router = APIRouter()
permission_router.include_router(
    get_permission_router, prefix="/permission", tags=["Permissions"]
)
permission_router.include_router(
    create_permission_router, prefix="/permission", tags=["Permissions"]
)
permission_router.include_router(
    update_permission_router, prefix="/permission", tags=["Permissions"]
)
permission_router.include_router(
    delete_permission_router, prefix="/permission", tags=["Permissions"]
)
