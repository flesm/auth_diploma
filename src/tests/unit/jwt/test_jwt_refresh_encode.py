import pytest
from jose import JWTError

from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


def test_jwt_encode_decode_refresh_valid_token_success(
    fake_jwt_encoder: FakeJwtTokenEncoder,
    id_for_refresh_token: str,
) -> None:
    token = fake_jwt_encoder.encode_refresh_token(user_id=id_for_refresh_token)
    user_id = fake_jwt_encoder.decode_refresh_token(token=token)
    assert user_id == id_for_refresh_token


def test_jwt_encode_decode_refresh_invalid_token_forbidden(
    fake_jwt_encoder: FakeJwtTokenEncoder,
    invalid_token: str,
) -> None:
    with pytest.raises(JWTError):
        fake_jwt_encoder.decode_refresh_token(token=invalid_token)
