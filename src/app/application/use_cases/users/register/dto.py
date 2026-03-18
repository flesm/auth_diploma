from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class RegisterUserRequestDTO:
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    role_id: UUID


@dataclass
class RegisterUserResponseDTO:
    id: UUID
    email: str
    first_name: str
    last_name: str
    role_id: UUID
    is_active: bool
    is_verified: bool
    created_at: datetime


@dataclass
class RegisteredUserWithTokenDTO:
    email: str
    token: str
