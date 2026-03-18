from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, BackgroundTasks, Depends
from starlette.responses import JSONResponse

from src.app.application.use_cases.users.forget_password.use_case import (
    ForgetPasswordUseCase,
)
from src.app.application.use_cases.users.reset_password.use_case import (
    ResetPasswordUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.user.reset_password.view_models import (  # noqa
    ResetPasswordRequestViewModel,
)

router = APIRouter()


@router.post("/forget")
@inject
async def forget_password(
    email: str,
    background_tasks: BackgroundTasks,
    forget_password_uc: ForgetPasswordUseCase = Depends(
        Provide[Container.forget_password]
    ),
) -> JSONResponse:

    background_tasks.add_task(forget_password_uc, email)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Reset link has been sent",
        },
    )


@router.post("/reset")
@inject
async def reset_password(
    view_model: ResetPasswordRequestViewModel,
    reset_password_uc: ResetPasswordUseCase = Depends(
        Provide[Container.reset_password]
    ),
) -> JSONResponse:
    dto = view_model.to_dto()
    await reset_password_uc(dto)
    return JSONResponse(
        status_code=200,
        content={
            "message": "Password has been successfully reseted",
        },
    )
