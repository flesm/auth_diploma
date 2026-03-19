from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class RoleEntity:
    id: UUID
    name: str
    description: str
    permissions: list = field(default_factory=list)
