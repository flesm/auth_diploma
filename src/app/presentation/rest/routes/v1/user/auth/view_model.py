from typing import Annotated

from pydantic import BaseModel, Field

from src.app.application.use_cases.users.auth.login.dto import LoginRequestDTO


class LoginUserRequestViewModel(BaseModel):
    email: str
    password: Annotated[str, Field(min_length=8)]

    def to_dto(self) -> LoginRequestDTO:
        return LoginRequestDTO(
            email=self.email,
            password=self.password,
        )
