from dataclasses import dataclass
from uuid import UUID


@dataclass
class UpdateRoleRequestDto:
    name: str
    description: str


@dataclass
class UpdateRoleResponseDto:
    id: UUID
    name: str
    description: str
