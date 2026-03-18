import pytest
from faker import Faker


@pytest.fixture
def payload_update_regular_role(faker: Faker) -> dict[str, str]:
    return {
        "name": faker.name(),
        "description": faker.random_letter(),
    }


@pytest.fixture
def payload_update_existed_regular_role(faker: Faker) -> dict[str, str]:
    return {
        "name": "name",
        "description": faker.random_letter(),
    }
