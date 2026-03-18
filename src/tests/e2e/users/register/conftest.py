import pytest
from faker import Faker


@pytest.fixture
def payload_register_regular_user(faker: Faker) -> dict[str, str]:
    return {
        "email": faker.unique.email(),
        "hashed_password": faker.password(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "role_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    }


@pytest.fixture
def url_register_user(url_v1: str) -> str:
    return f"{url_v1}/user/register"
