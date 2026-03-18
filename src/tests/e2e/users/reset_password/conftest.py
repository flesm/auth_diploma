import pytest
from faker import Faker

from src.app.infra.jwt.jwt_encoder import JwtTokenEncoder


@pytest.fixture
def reset_token_of_unverified_user(
    unverified_regular_user: str, jwt_encoder: JwtTokenEncoder
) -> str:
    return jwt_encoder.encode_reset_token(email=unverified_regular_user)


@pytest.fixture
def invalid_reset_token() -> str:
    return (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJzdWIiOiJzaGFubm9uc2NobWlkdEBleGFtcGxlLmNvbSIsImV4cCI6MTc1MD"
        "czNDk3NX0.T8p7OTarFO_ahNz1vA65t-e52Pad__v6LjyV7lh9u2s"
    )


@pytest.fixture
def payload_reset_password_regular_user(
    faker: Faker, reset_token_of_unverified_user: str
) -> dict[str, str]:
    return {
        "token": reset_token_of_unverified_user,
        "new_password": faker.password(),
    }


@pytest.fixture
def payload_reset_password_invalid_reset_link(
    faker: Faker, invalid_reset_token: str
) -> dict[str, str]:
    return {"token": invalid_reset_token, "new_password": faker.password()}


@pytest.fixture
def url_forget_password(url_v1: str) -> str:
    return f"{url_v1}/reset_password/forget"


@pytest.fixture
def url_reset_password(url_v1: str) -> str:
    return f"{url_v1}/reset_password/reset"
