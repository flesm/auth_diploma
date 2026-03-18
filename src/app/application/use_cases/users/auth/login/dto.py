from dataclasses import dataclass


@dataclass
class LoginRequestDTO:
    email: str
    password: str


@dataclass
class LoginResponseDTO:
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
