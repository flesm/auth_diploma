from datetime import datetime, timedelta
from typing import Any, cast

from jose import ExpiredSignatureError, JWTError, jwt

from src.app.application.interfaces.jwt.jwt_encoder import IJwtTokenEncoder
from src.app.application.use_cases.users.exceptions import (
    InvalidOrExpiredTokenException,
)
from src.app.application.use_cases.users.reset_password.exceptions import (
    InvalidOrExpiredResetLink,
)
from src.app.config import Config


class JwtTokenEncoder(IJwtTokenEncoder):

    def __init__(self, config: Config) -> None:
        self._reset_secret_key = config.JWT.forget_pwd_secret_key
        self._verify_secret_key = config.JWT.verify_email_secret_key
        self._expire_minute = config.JWT.expire_minutes

        self._access_secret_key = config.JWT.access_secret_key
        self._refresh_secret_key = config.JWT.refresh_secret_key
        self._access_expire_minutes = config.JWT.access_expire_minutes
        self._refresh_expire_minutes = config.JWT.refresh_expire_minutes

        self._algorithm = config.JWT.algorithm

    def _encode(
        self,
        secret_key: str | None,
        payload: dict[str, Any],
        expire_minutes: int,
    ) -> str:
        payload = {
            **payload,
            "exp": datetime.now() + timedelta(minutes=float(expire_minutes)),
        }
        token = jwt.encode(payload, secret_key, algorithm=self._algorithm)
        return cast(str, token)

    def _decode(self, secret_key: str | None, token: str) -> Any:
        return jwt.decode(token, secret_key, algorithms=[self._algorithm])

    def encode_reset_token(self, email: str) -> str:
        return self._encode(
            secret_key=self._reset_secret_key,
            payload={"sub": email},
            expire_minutes=self._expire_minute,
        )

    def encode_verify_token(self, email: str) -> str:
        return self._encode(
            secret_key=self._verify_secret_key,
            payload={"sub": email},
            expire_minutes=self._expire_minute,
        )

    def encode_access_token(
        self,
        user_id: str,
        username: str,
        is_staff: bool,
        email: str,
        role: str,
    ) -> str:
        return self._encode(
            secret_key=self._access_secret_key,
            payload={
                "user_id": user_id,
                "username": username,
                "is_staff": is_staff,
                "email": email,
                "role": role,
            },
            expire_minutes=self._access_expire_minutes,
        )

    def encode_refresh_token(self, user_id: str) -> str:
        return self._encode(
            secret_key=self._refresh_secret_key,
            payload={"sub": user_id},
            expire_minutes=self._refresh_expire_minutes,
        )

    def decode_reset_token(self, token: str) -> Any:
        try:
            return self._decode(self._reset_secret_key, token)["sub"]
        except (ExpiredSignatureError, JWTError):
            raise InvalidOrExpiredResetLink("Invalid or expired reset link")

    def decode_verify_token(self, token: str) -> Any:
        try:
            return self._decode(self._verify_secret_key, token)["sub"]
        except (ExpiredSignatureError, JWTError):
            raise InvalidOrExpiredTokenException(
                "Invalid or expired verification token."
            )

    def decode_access_token(self, token: str) -> Any:
        try:
            return self._decode(self._access_secret_key, token)
        except (ExpiredSignatureError, JWTError):
            raise JWTError("Invalid or expired access token.")

    def decode_refresh_token(self, token: str) -> Any:
        try:
            return self._decode(self._refresh_secret_key, token)["sub"]
        except (ExpiredSignatureError, JWTError):
            raise JWTError("Invalid or expired refresh token.")
