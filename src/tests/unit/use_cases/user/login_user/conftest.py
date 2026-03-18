import pytest
from faker import Faker

from src.app.application.use_cases.users.auth.login.dto import LoginRequestDTO


@pytest.fixture
def login_foreign_user_dto(faker: Faker) -> LoginRequestDTO:
    return LoginRequestDTO(email=faker.email(), password=faker.password())
