from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreatePermissionRequestDto:
    name: str
    description: str


@dataclass
class CreatePermissionResponseDto:
    id: UUID
    name: str
    description: str
