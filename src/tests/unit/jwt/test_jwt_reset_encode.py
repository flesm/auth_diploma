import pytest
from jose import JWTError

from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


class TestJwtResetEncode:

    def test_case_1(
        self,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        reset_password_email: str,
    ) -> None:
            token = fake_jwt_encoder.encode_reset_token(email=reset_password_email)
            email = fake_jwt_encoder.decode_reset_token(token=token)
            assert email == reset_password_email

    def test_case_2(
        self,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        invalid_token: str,
    ) -> None:
            with pytest.raises(JWTError):
                fake_jwt_encoder.decode_reset_token(token=invalid_token)
