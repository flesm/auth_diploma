from dataclasses import dataclass
from uuid import UUID


@dataclass
class PermissionEntity:
    id: UUID
    name: str
    description: str
