from dataclasses import dataclass
from uuid import UUID


@dataclass
class CurrentUserResponseDto:
    id: UUID
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_verified: bool
    is_staff: bool
