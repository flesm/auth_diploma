from datetime import datetime
from typing import Annotated, Self
from uuid import UUID

from pydantic import BaseModel, Field

from src.app.application.entities.user import UserEntity
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
    RegisterUserResponseDTO,
)


class RegisterUserRequestViewModel(BaseModel):
    email: str
    hashed_password: Annotated[str, Field(min_length=8)]
    first_name: str
    last_name: str
    role_id: UUID

    def to_dto(self) -> RegisterUserRequestDTO:
        return RegisterUserRequestDTO(
            email=self.email,
            hashed_password=self.hashed_password,
            first_name=self.first_name,
            last_name=self.last_name,
            role_id=self.role_id,
        )


class RegisterUserResponseViewModel(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    role_id: UUID
    is_active: bool
    is_verified: bool
    created_at: datetime

    @classmethod
    def to_view_model(cls, dto: RegisterUserResponseDTO) -> Self:
        return cls(
            id=dto.id,
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            role_id=dto.role_id,
            is_active=dto.is_active,
            is_verified=dto.is_verified,
            created_at=dto.created_at,
        )

    @classmethod
    def from_entity(cls, entity: UserEntity) -> Self:
        return cls(
            id=entity.id,
            email=entity.email,
            first_name=entity.first_name,
            last_name=entity.last_name,
            role_id=entity.role_id,
            is_active=entity.is_active,
            is_verified=entity.is_verified,
            created_at=entity.created_at,
        )
