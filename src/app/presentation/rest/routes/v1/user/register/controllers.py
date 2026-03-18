from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, BackgroundTasks, Depends

from src.app.application.use_cases.users.register.use_case import (
    RegisterUserUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.user.register.view_models import (
    RegisterUserRequestViewModel,
    RegisterUserResponseViewModel,
)

router = APIRouter()


@router.post("/register", response_model=RegisterUserResponseViewModel)
@inject
async def register_user(
    view_model: RegisterUserRequestViewModel,
    background_tasks: BackgroundTasks,
    register_user_uc: RegisterUserUseCase = Depends(
        Provide[Container.register_user]
    ),
) -> RegisterUserResponseViewModel:
    dto = view_model.to_dto()

    user = await register_user_uc.create_user(dto=dto)

    background_tasks.add_task(
        register_user_uc.send_verification_email, user.email
    )

    return RegisterUserResponseViewModel.from_entity(user)
