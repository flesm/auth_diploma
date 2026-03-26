import pytest
from jose import JWTError

from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder


class TestJwtVerifyEncode:

    def test_case_1(
        self,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        verify_email: str,
    ) -> None:
            token = fake_jwt_encoder.encode_verify_token(email=verify_email)
            email = fake_jwt_encoder.decode_verify_token(token=token)
            assert email == verify_email

    def test_case_2(
        self,
        fake_jwt_encoder: FakeJwtTokenEncoder,
        invalid_token: str,
    ) -> None:
            with pytest.raises(JWTError):
                fake_jwt_encoder.decode_verify_token(token=invalid_token)
