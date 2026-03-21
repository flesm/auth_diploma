from typing import Any

import pytest
from faker import Faker


@pytest.fixture
def verify_email() -> str:
    return "verify@example.com"


@pytest.fixture
def reset_password_email() -> str:
    return "reset_password@example.com"


@pytest.fixture
def payload_for_access_token(faker: Faker) -> dict[str, Any]:
    return {
        "user_id": "46ade0f6-cde8-4244-a2e7-a9618652c072",
        "user_name": faker.first_name(),
        "is_staff": False,
        "email": faker.email(),
        "role": "intern",
    }


@pytest.fixture
def id_for_refresh_token() -> str:
    return "56ade0f6-cde8-4244-a2e7-a9618652c072"
