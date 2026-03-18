from datetime import datetime
from typing import Generator
from uuid import UUID, uuid4

import pytest
import pytest_asyncio
from faker import Faker

from src.app.application.entities.permission import PermissionEntity
from src.app.application.entities.role import RoleEntity
from src.app.application.entities.user import UserEntity
from src.app.application.use_cases.users.auth.login.dto import LoginRequestDTO
from src.app.application.use_cases.users.auth.login.use_case import (
    LoginUseCase,
)
from src.app.application.use_cases.users.register.dto import (
    RegisterUserRequestDTO,
)
from src.tests.environment.crypto.password_cryptografer import (
    FakePasswordCryptografer,
)
from src.tests.environment.jwt.jwt_encoder import FakeJwtTokenEncoder
from src.tests.environment.uow.unit_of_work import FakeSQLAUnitOfWork


@pytest.fixture
def fake_uow() -> Generator[FakeSQLAUnitOfWork, None, None]:
    uow = FakeSQLAUnitOfWork()
    yield uow
    uow.users.users.clear()
    uow.permissions.permissions.clear()
    uow.roles.roles.clear()
    uow.roles_permissions.role_permissions.clear()


@pytest.fixture
def register_regular_user_dto(faker: Faker) -> RegisterUserRequestDTO:
    return RegisterUserRequestDTO(
        email=faker.unique.email(),
        hashed_password=faker.password(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        role_id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    )


@pytest.fixture
def non_existent_email() -> str:
    return "nonexistent@example.com"


@pytest.fixture
def role_id(faker: Faker, fake_uow: FakeSQLAUnitOfWork) -> UUID:
    role = RoleEntity(
        id=uuid4(),
        name=faker.name(),
        description=faker.random_letter(),
    )

    fake_uow.roles.roles.append(role)

    return role.id


@pytest.fixture
def another_role_id(faker: Faker, fake_uow: FakeSQLAUnitOfWork) -> UUID:
    role = RoleEntity(
        id=uuid4(),
        name=faker.name(),
        description=faker.random_letter(),
    )

    fake_uow.roles.roles.append(role)

    return role.id


@pytest.fixture
def foreign_role_id() -> UUID:
    return uuid4()


@pytest.fixture
def permission_id(faker: Faker, fake_uow: FakeSQLAUnitOfWork) -> UUID:
    permission = PermissionEntity(
        id=uuid4(),
        name=faker.name(),
        description=faker.random_letter(),
    )

    fake_uow.permissions.permissions.append(permission)

    return permission.id


@pytest.fixture
def another_permission_id(faker: Faker, fake_uow: FakeSQLAUnitOfWork) -> UUID:
    permission = PermissionEntity(
        id=uuid4(),
        name=faker.name(),
        description=faker.random_letter(),
    )

    fake_uow.permissions.permissions.append(permission)

    return permission.id


@pytest.fixture
def foreign_permission_id() -> UUID:
    return uuid4()


@pytest.fixture
def login_existed_user_dto(
    fake_uow: FakeSQLAUnitOfWork,
    faker: Faker,
    fake_password_cryptografer: FakePasswordCryptografer,
) -> LoginRequestDTO:

    email = faker.email()
    password = faker.password()

    hashed_password = fake_password_cryptografer.hash(password=password)

    user = UserEntity(
        id=uuid4(),
        email=email,
        hashed_password=hashed_password,
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        is_active=True,
        is_verified=False,
        role_id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    fake_uow.users.users.append(user)

    return LoginRequestDTO(email=email, password=password)


@pytest.fixture
def login_user_uc(
    fake_uow: FakeSQLAUnitOfWork,
    fake_jwt_encoder: FakeJwtTokenEncoder,
    fake_password_cryptografer: FakePasswordCryptografer,
) -> LoginUseCase:
    return LoginUseCase(
        rdbms_uow=fake_uow,
        jwt_encoder=fake_jwt_encoder,
        password_cryptografer=fake_password_cryptografer,
    )


@pytest_asyncio.fixture
async def access_token_of_regular_user(
    login_existed_user_dto: LoginRequestDTO, login_user_uc: LoginUseCase
) -> str:
    result = await login_user_uc(dto=login_existed_user_dto)

    return result.access_token
