import pytest

from src.app.infra.jwt.jwt_encoder import JwtTokenEncoder


@pytest.fixture
def verify_token_of_verified_user(
    verified_regular_user: str, jwt_encoder: JwtTokenEncoder
) -> str:
    return jwt_encoder.encode_verify_token(email=verified_regular_user)


@pytest.fixture
def verify_token_of_unverified_user(
    unverified_regular_user: str, jwt_encoder: JwtTokenEncoder
) -> str:
    return jwt_encoder.encode_verify_token(email=unverified_regular_user)


@pytest.fixture
def url_verify_email(url_v1: str) -> str:
    return f"{url_v1}/verify_email/verify"


@pytest.fixture
def url_resend_verification(url_v1: str) -> str:
    return f"{url_v1}/verify_email/resend_verification"
