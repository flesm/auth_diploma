from typing import cast

from passlib.context import CryptContext

from src.app.application.interfaces.crypto.password_cryptografer import (
    IPasswordCryptografer,
)


class CCPasswordCryptografer(IPasswordCryptografer):
    def __init__(self) -> None:
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        return cast(str, self._pwd_context.hash(password))

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return bool(self._pwd_context.verify(plain_password, hashed_password))
