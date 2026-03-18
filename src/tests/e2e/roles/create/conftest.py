import pytest
from faker import Faker


@pytest.fixture
def payload_create_regular_role(faker: Faker) -> dict[str, str]:
    return {
        "name": faker.name(),
        "description": faker.random_letter(),
    }
