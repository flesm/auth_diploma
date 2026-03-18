import pytest

from src.app.application.use_cases.roles.get.controllers import (
    GetRoleByIdUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_role_by_id_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> GetRoleByIdUseCase:
    return GetRoleByIdUseCase(rdbms_uow=fake_uow)
