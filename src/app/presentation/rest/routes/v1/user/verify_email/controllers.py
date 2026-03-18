from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.app.application.use_cases.users.resend_verification.use_case import (
    ResendVerificationEmailUseCase,
)
from src.app.application.use_cases.users.verify_email.use_cases import (
    VerifyUserUseCase,
)
from src.app.container import Container

router = APIRouter()


@router.get("/verify")
@inject
async def verify_user(
    token: str,
    verify_email_uc: VerifyUserUseCase = Depends(
        Provide[Container.verify_user]
    ),
) -> JSONResponse:

    await verify_email_uc(token=token)

    return JSONResponse(
        status_code=200,
        content={
            "message": "User successfully verified",
        },
    )


@router.post("/resend_verification")
@inject
async def resend_verification(
    email: str,
    resend_verification_uc: ResendVerificationEmailUseCase = Depends(
        Provide[Container.resend_verification]
    ),
) -> JSONResponse:
    await resend_verification_uc(email=email)
    return JSONResponse(
        status_code=200,
        content={
            "message": "Verification successfully resend",
            "data": email,
        },
    )
