from fastapi import APIRouter

from src.app.presentation.rest.routes.v1.role.create.controllers import (
    router as create_role_router,
)
from src.app.presentation.rest.routes.v1.role.delete.controllers import (
    router as delete_role_router,
)
from src.app.presentation.rest.routes.v1.role.get.controllers import (
    router as get_role_router,
)
from src.app.presentation.rest.routes.v1.role.update.controllers import (
    router as update_role_router,
)

role_router = APIRouter()
role_router.include_router(get_role_router, prefix="/role", tags=["Roles"])
role_router.include_router(create_role_router, prefix="/role", tags=["Roles"])
role_router.include_router(update_role_router, prefix="/role", tags=["Roles"])
role_router.include_router(delete_role_router, prefix="/role", tags=["Roles"])
