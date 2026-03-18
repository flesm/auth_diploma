from dataclasses import dataclass


@dataclass
class ResetPasswordRequestDTO:
    token: str
    new_password: str
