import pytest

from src.app.application.use_cases.roles.get.controllers import (
    GetAllRolesUseCase,
)
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def get_all_roles_uc(
    fake_uow: FakeSQLAUnitOfWork,
) -> GetAllRolesUseCase:
    return GetAllRolesUseCase(rdbms_uow=fake_uow)
