from datetime import datetime
from uuid import UUID, uuid4

import pytest
from faker import Faker

from src.app.application.entities.user import UserEntity
from src.app.application.use_cases.users.profile.get.use_case import (
    ListUsersUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_list_of_user_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> ListUsersUseCase:
    return ListUsersUseCase(
        rdbms_uow=fake_uow,
    )


@pytest.fixture
def user_with_admin_role(
    fake_uow: FakeSQLAUnitOfWork, faker: Faker
) -> UserEntity:
    user = UserEntity(
        id=uuid4(),
        email=faker.unique.email(),
        hashed_password=faker.password(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        is_active=True,
        is_verified=False,
        role_id=UUID("5fa85f64-5717-4562-b3fc-2c963f66afa6"),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    fake_uow.users.users.append(user)

    return user


@pytest.fixture
def user_with_superadmin_role(
    fake_uow: FakeSQLAUnitOfWork, faker: Faker
) -> UserEntity:
    user = UserEntity(
        id=uuid4(),
        email=faker.unique.email(),
        hashed_password=faker.password(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        is_active=True,
        is_verified=False,
        role_id=UUID("8fa85f64-5717-4562-b3fc-2c963f66afa6"),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    fake_uow.users.users.append(user)

    return user
