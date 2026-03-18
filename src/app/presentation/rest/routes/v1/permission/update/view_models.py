from typing import Self
from uuid import UUID

from pydantic import BaseModel

from src.app.application.entities.permission import PermissionEntity
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
    UpdatePermissionResponseDto,
)


class UpdatePermissionRequestViewModel(BaseModel):
    name: str
    description: str

    def to_dto(self) -> UpdatePermissionRequestDto:
        return UpdatePermissionRequestDto(
            name=self.name,
            description=self.description,
        )


class UpdatePermissionResponseViewModel(BaseModel):
    id: UUID
    name: str
    description: str

    @classmethod
    def to_view_model(cls, dto: UpdatePermissionResponseDto) -> Self:
        return cls(id=dto.id, name=dto.name, description=dto.description)

    @classmethod
    def from_entity(cls, entity: PermissionEntity) -> Self:
        return cls(
            id=entity.id, name=entity.name, description=entity.description
        )
