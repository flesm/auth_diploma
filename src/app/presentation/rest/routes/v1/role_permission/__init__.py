from fastapi import APIRouter

from src.app.presentation.rest.routes.v1.role_permission.attach.controllers import (  # noqa
    router as attach_role_permission_router,
)
from src.app.presentation.rest.routes.v1.role_permission.detach.controllers import (  # noqa
    router as detach_role_permission_router,
)

role_permission_router = APIRouter()
role_permission_router.include_router(attach_role_permission_router)
role_permission_router.include_router(detach_role_permission_router)
