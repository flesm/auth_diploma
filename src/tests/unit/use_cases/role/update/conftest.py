from uuid import UUID

import pytest
from faker import Faker

from src.app.application.use_cases.roles.get.controllers import (
    GetRoleByIdUseCase,
)
from src.app.application.use_cases.roles.update.dto import UpdateRoleRequestDto
from src.app.application.use_cases.roles.update.use_case import (
    UpdateRoleUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def update_role_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> UpdateRoleUseCase:
    return UpdateRoleUseCase(rdbms_uow=fake_uow)


@pytest.fixture
def role_dto(faker: Faker) -> UpdateRoleRequestDto:
    return UpdateRoleRequestDto(
        name=faker.name(),
        description=faker.random_letter(),
    )


@pytest.fixture
async def existing_role_dto(
    faker: Faker, role_id: UUID, get_role_by_id_uc: GetRoleByIdUseCase
) -> UpdateRoleRequestDto:
    role = await get_role_by_id_uc(role_id=role_id)

    return UpdateRoleRequestDto(
        name=role.name,
        description=faker.random_letter(),
    )
