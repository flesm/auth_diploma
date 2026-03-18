from dataclasses import dataclass
from uuid import UUID


@dataclass
class RoleEntity:
    id: UUID
    name: str
    description: str
