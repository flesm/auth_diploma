from uuid import uuid4

import pytest
from faker import Faker

from src.app.application.entities.permission import PermissionEntity
from src.app.application.use_cases.permissions.create.dto import (
    CreatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.create.use_case import (
    CreatePermissionUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def create_permission_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> CreatePermissionUseCase:
    return CreatePermissionUseCase(rdbms_uow=fake_uow)


@pytest.fixture
def permission_dto(faker: Faker) -> CreatePermissionRequestDto:
    return CreatePermissionRequestDto(
        name=faker.name(),
        description=faker.random_letter(),
    )


@pytest.fixture
def existed_permission_dto(
    fake_uow: FakeSQLAUnitOfWork, faker: Faker
) -> CreatePermissionRequestDto:
    permission_id = uuid4()
    name = faker.name()
    description = faker.random_letter()

    permission = PermissionEntity(
        id=permission_id,
        name=name,
        description=description,
    )

    fake_uow.permissions.permissions.append(permission)

    return CreatePermissionRequestDto(
        name=name,
        description=description,
    )
