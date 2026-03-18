from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class UserEntity:
    id: UUID
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    is_active: bool
    is_verified: bool
    role_id: UUID
    created_at: datetime
    updated_at: datetime
