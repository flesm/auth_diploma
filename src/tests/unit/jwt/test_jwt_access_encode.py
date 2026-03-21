import pytest
from jose import JWTError

from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


def test_jwt_encode_decode_access_valid_token_success(
    fake_jwt_encoder: FakeJwtTokenEncoder,
    payload_for_access_token: dict[str, str],
) -> None:
    token = fake_jwt_encoder.encode_access_token(
        user_id=payload_for_access_token.get("user_id"),
        username=payload_for_access_token.get("username"),
        is_staff=bool(payload_for_access_token.get("is_staff")),
        email=payload_for_access_token.get("email"),
        role=payload_for_access_token.get("role"),
    )
    user = fake_jwt_encoder.decode_access_token(token=token)
    assert user.get("user_id") == payload_for_access_token.get("user_id")
    assert user.get("role") == payload_for_access_token.get("role")


def test_jwt_encode_decode_access_invalid_token_forbidden(
    fake_jwt_encoder: FakeJwtTokenEncoder,
    invalid_token: str,
) -> None:
    with pytest.raises(JWTError):
        fake_jwt_encoder.decode_access_token(token=invalid_token)
