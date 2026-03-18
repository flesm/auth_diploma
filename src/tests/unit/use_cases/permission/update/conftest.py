from uuid import UUID

import pytest
from faker import Faker

from src.app.application.use_cases.permissions.get.use_case import (
    GetPermissionByIdUseCase,
)
from src.app.application.use_cases.permissions.update.dto import (
    UpdatePermissionRequestDto,
)
from src.app.application.use_cases.permissions.update.use_case import (
    UpdatePermissionUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def update_permission_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> UpdatePermissionUseCase:
    return UpdatePermissionUseCase(rdbms_uow=fake_uow)


@pytest.fixture
def permission_dto(faker: Faker) -> UpdatePermissionRequestDto:
    return UpdatePermissionRequestDto(
        name=faker.name(),
        description=faker.random_letter(),
    )


@pytest.fixture
async def existing_permission_dto(
    faker: Faker,
    permission_id: UUID,
    get_permission_by_id_uc: GetPermissionByIdUseCase,
) -> UpdatePermissionRequestDto:
    permission = await get_permission_by_id_uc(permission_id)

    return UpdatePermissionRequestDto(
        name=permission.name,
        description=faker.random_letter(),
    )
