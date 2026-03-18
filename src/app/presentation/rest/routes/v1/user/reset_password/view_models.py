from pydantic import BaseModel, Field

from src.app.application.use_cases.users.reset_password.dto import (
    ResetPasswordRequestDTO,
)


class ResetPasswordRequestViewModel(BaseModel):
    token: str
    new_password: str = Field(min_length=8)

    def to_dto(self) -> ResetPasswordRequestDTO:
        return ResetPasswordRequestDTO(
            token=self.token,
            new_password=self.new_password,
        )
