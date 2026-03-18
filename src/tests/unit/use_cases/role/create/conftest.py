from uuid import uuid4

import pytest
from faker import Faker

from src.app.application.entities.role import RoleEntity
from src.app.application.use_cases.roles.create.dto import CreateRoleRequestDto
from src.app.application.use_cases.roles.create.use_case import (
    CreateRoleUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def create_role_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> CreateRoleUseCase:
    return CreateRoleUseCase(rdbms_uow=fake_uow)


@pytest.fixture
def role_dto(faker: Faker) -> CreateRoleRequestDto:
    return CreateRoleRequestDto(
        name=faker.name(),
        description=faker.random_letter(),
    )


@pytest.fixture
def existed_role_dto(
    fake_uow: FakeSQLAUnitOfWork, faker: Faker
) -> CreateRoleRequestDto:
    role_id = uuid4()
    name = faker.name()
    description = faker.random_letter()

    role = RoleEntity(
        id=role_id,
        name=name,
        description=description,
    )

    fake_uow.roles.roles.append(role)

    return CreateRoleRequestDto(
        name=name,
        description=description,
    )
