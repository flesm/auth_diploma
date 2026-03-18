from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.application.use_cases.users.auth.get_current_user.dto import (
    CurrentUserResponseDto,
)
from src.app.application.use_cases.users.auth.get_current_user.use_case import (  # noqa
    GetCurrentUserUseCase,
)
from src.app.application.use_cases.users.auth.login.dto import LoginResponseDTO
from src.app.application.use_cases.users.auth.login.use_case import (
    LoginUseCase,
)
from src.app.application.use_cases.users.auth.refresh.use_case import (
    RefreshTokenUseCase,
)
from src.app.container import Container
from src.app.presentation.rest.routes.v1.user.auth.view_model import (
    LoginUserRequestViewModel,
)

router = APIRouter()


@router.post("/login", response_model=LoginResponseDTO)
@inject
async def login(
    view_model: LoginUserRequestViewModel,
    login_uc: LoginUseCase = Depends(Provide[Container.login_user]),
) -> LoginResponseDTO:
    dto = view_model.to_dto()

    return await login_uc(dto)


@router.post("/token/refresh")
@inject
async def refresh_token(
    token: str,
    refresh_uc: RefreshTokenUseCase = Depends(
        Provide[Container.refresh_token]
    ),
) -> str:
    return await refresh_uc(refresh_token=token)


@router.get("/me")
@inject
async def get_me(
    token: str,
    get_me_uc: GetCurrentUserUseCase = Depends(
        Provide[Container.get_current_user]
    ),
) -> CurrentUserResponseDto:
    return await get_me_uc(token)
