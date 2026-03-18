from fastapi import APIRouter

from src.app.presentation.rest.routes.v1.permission import permission_router
from src.app.presentation.rest.routes.v1.role import role_router
from src.app.presentation.rest.routes.v1.role_permission import (
    role_permission_router,
)
from src.app.presentation.rest.routes.v1.user.auth.controllers import (
    router as auth_router,
)
from src.app.presentation.rest.routes.v1.user.profile.controllers import (
    router as profile_router,
)
from src.app.presentation.rest.routes.v1.user.register.controllers import (
    router as user_router,
)
from src.app.presentation.rest.routes.v1.user.reset_password.controllers import (  # noqa
    router as reset_pass_router,
)
from src.app.presentation.rest.routes.v1.user.verify_email.controllers import (
    router as verify_email_router,
)

v1_router = APIRouter()


v1_router.include_router(user_router, prefix="/user", tags=["User"])
v1_router.include_router(
    reset_pass_router, prefix="/reset_password", tags=["Reset Password"]
)
v1_router.include_router(
    verify_email_router, prefix="/verify_email", tags=["Verify Email"]
)
v1_router.include_router(permission_router)
v1_router.include_router(role_router)
v1_router.include_router(
    role_permission_router,
    prefix="/role_permission",
    tags=["RolesPermissions"],
)
v1_router.include_router(profile_router, prefix="/profile", tags=["Profile"])
v1_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
