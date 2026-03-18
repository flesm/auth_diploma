from typing import Self
from uuid import UUID

from pydantic import BaseModel

from src.app.application.entities.role import RoleEntity
from src.app.application.use_cases.roles.update.dto import (
    UpdateRoleRequestDto,
    UpdateRoleResponseDto,
)


class UpdateRoleRequestViewModel(BaseModel):
    name: str
    description: str

    def to_dto(self) -> UpdateRoleRequestDto:
        return UpdateRoleRequestDto(
            name=self.name,
            description=self.description,
        )


class UpdateRoleResponseViewModel(BaseModel):
    id: UUID
    name: str
    description: str

    @classmethod
    def to_view_model(cls, dto: UpdateRoleResponseDto) -> Self:
        return cls(id=dto.id, name=dto.name, description=dto.description)

    @classmethod
    def from_entity(cls, entity: RoleEntity) -> Self:
        return cls(
            id=entity.id, name=entity.name, description=entity.description
        )
