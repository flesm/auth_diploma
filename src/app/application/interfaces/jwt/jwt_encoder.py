from abc import ABC, abstractmethod
from typing import Any


class IJwtTokenEncoder(ABC):
    def _encode(
        self,
        secret_key: str | None,
        payload: dict[str, Any],
        expire_minutes: int,
    ) -> str:
        raise NotImplementedError()

    def _decode(self, secret_key: str, token: str) -> dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    def encode_reset_token(self, email: str) -> str:
        pass

    @abstractmethod
    def encode_verify_token(self, email: str) -> str:
        pass

    @abstractmethod
    def encode_access_token(
        self,
        user_id: str,
        username: str,
        is_staff: bool,
        email: str,
        role: str,
    ) -> str:
        pass

    @abstractmethod
    def encode_refresh_token(self, user_id: str) -> str:
        pass

    @abstractmethod
    def decode_reset_token(self, token: str) -> str:
        pass

    @abstractmethod
    def decode_verify_token(self, token: str) -> str:
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> dict[str, str]:
        pass

    @abstractmethod
    def decode_refresh_token(self, token: str) -> str:
        pass
