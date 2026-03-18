from dataclasses import dataclass
from uuid import UUID


@dataclass
class UpdatePermissionRequestDto:
    name: str
    description: str


@dataclass
class UpdatePermissionResponseDto:
    id: UUID
    name: str
    description: str
