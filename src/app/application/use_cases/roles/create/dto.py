from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateRoleRequestDto:
    name: str
    description: str


@dataclass
class CreateRoleResponseDto:
    id: UUID
    name: str
    description: str
