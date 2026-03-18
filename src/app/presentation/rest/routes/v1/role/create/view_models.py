from typing import Self
from uuid import UUID

from pydantic import BaseModel

from src.app.application.entities.role import RoleEntity
from src.app.application.use_cases.roles.create.dto import (
    CreateRoleRequestDto,
    CreateRoleResponseDto,
)


class CreateRoleRequestViewModel(BaseModel):
    name: str
    description: str

    def to_dto(self) -> CreateRoleRequestDto:
        return CreateRoleRequestDto(
            name=self.name,
            description=self.description,
        )


class CreateRoleResponseViewModel(BaseModel):
    id: UUID
    name: str
    description: str

    @classmethod
    def to_view_model(cls, dto: CreateRoleResponseDto) -> Self:
        return cls(id=dto.id, name=dto.name, description=dto.description)

    @classmethod
    def from_entity(cls, entity: RoleEntity) -> Self:
        return cls(
            id=entity.id, name=entity.name, description=entity.description
        )
