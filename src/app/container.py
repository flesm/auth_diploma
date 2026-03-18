from dependency_injector import containers, providers

from src.app.application.use_cases.permissions.create.use_case import (
    CreatePermissionUseCase,
)
from src.app.application.use_cases.permissions.delete.use_case import (
    DeletePermissionUseCase,
)
from src.app.application.use_cases.permissions.get.use_case import (
    GetAllPermissionsUseCase,
    GetPermissionByIdUseCase,
)
from src.app.application.use_cases.permissions.update.use_case import (
    UpdatePermissionUseCase,
)
from src.app.application.use_cases.roles.create.use_case import (
    CreateRoleUseCase,
)
from src.app.application.use_cases.roles.delete.controllers import (
    DeleteRoleUseCase,
)
from src.app.application.use_cases.roles.get.controllers import (
    GetAllRolesUseCase,
    GetRoleByIdUseCase,
)
from src.app.application.use_cases.roles.update.use_case import (
    UpdateRoleUseCase,
)
from src.app.application.use_cases.roles_permissions.attach.use_case import (
    AttachPermissionToRoleUseCase,
)
from src.app.application.use_cases.roles_permissions.detach.use_case import (
    DetachRoleWithPermissionUseCase,
)
from src.app.application.use_cases.users.auth.get_current_user.use_case import (  # noqa
    GetCurrentUserUseCase,
)
from src.app.application.use_cases.users.auth.login.use_case import (
    LoginUseCase,
)
from src.app.application.use_cases.users.auth.refresh.use_case import (
    RefreshTokenUseCase,
)
from src.app.application.use_cases.users.forget_password.use_case import (
    ForgetPasswordUseCase,
)
from src.app.application.use_cases.users.profile.delete.use_case import (
    DeleteProfileUseCase,
)
from src.app.application.use_cases.users.profile.get.use_case import (
    ListUsersUseCase,
)
from src.app.application.use_cases.users.profile.update.use_case import (
    UpdateProfileUseCase,
)
from src.app.application.use_cases.users.register.use_case import (
    RegisterUserUseCase,
)
from src.app.application.use_cases.users.resend_verification.use_case import (
    ResendVerificationEmailUseCase,
)
from src.app.application.use_cases.users.reset_password.use_case import (
    ResetPasswordUseCase,
)
from src.app.application.use_cases.users.verify_email.use_cases import (
    VerifyUserUseCase,
)
from src.app.config import Config
from src.app.infra.api_clients.email.email_config import provide_mail_config
from src.app.infra.connection_engines.sqla.db import Database
from src.app.infra.crypto.password_cryptografer import CCPasswordCryptografer
from src.app.infra.email.email_sender import FMEmailSender
from src.app.infra.jwt.jwt_encoder import JwtTokenEncoder
from src.app.infra.unit_of_work.sqla import SQLAUnitOfWork


class DBContainer(containers.DeclarativeContainer):
    config = providers.Dependency(instance_of=Config)
    db = providers.Resource(Database, config=config.provided.DB)
    uow = providers.Factory(
        SQLAUnitOfWork, session_factory=db.provided.session_factory
    )


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Config)

    db = providers.Container(DBContainer, config=config)

    mail_config = providers.Singleton(
        provide_mail_config,
        config=config,
    )

    email_sender = providers.Singleton(
        FMEmailSender, config=config, mail_config=mail_config
    )
    jwt_encoder = providers.Singleton(JwtTokenEncoder, config=config)
    password_cryptografer = providers.Singleton(CCPasswordCryptografer)

    register_user = providers.Factory(
        RegisterUserUseCase,
        rdbms_uow=db.container.uow,
        email_sender=email_sender,
        jwt_encoder=jwt_encoder,
        password_cryptografer=password_cryptografer,
    )

    forget_password = providers.Factory(
        ForgetPasswordUseCase,
        rdbms_uow=db.container.uow,
        email_sender=email_sender,
        jwt_encoder=jwt_encoder,
    )

    reset_password = providers.Factory(
        ResetPasswordUseCase,
        rdbms_uow=db.container.uow,
        email_sender=email_sender,
        jwt_encoder=jwt_encoder,
        password_cryptografer=password_cryptografer,
    )

    resend_verification = providers.Factory(
        ResendVerificationEmailUseCase,
        rdbms_uow=db.container.uow,
        email_sender=email_sender,
        jwt_encoder=jwt_encoder,
    )

    verify_user = providers.Factory(
        VerifyUserUseCase,
        rdbms_uow=db.container.uow,
        jwt_encoder=jwt_encoder,
    )

    get_permission_by_id = providers.Factory(
        GetPermissionByIdUseCase, rdbms_uow=db.container.uow
    )

    get_all_permissions = providers.Factory(
        GetAllPermissionsUseCase, rdbms_uow=db.container.uow
    )

    create_permission = providers.Factory(
        CreatePermissionUseCase, rdbms_uow=db.container.uow
    )

    update_permission = providers.Factory(
        UpdatePermissionUseCase, rdbms_uow=db.container.uow
    )

    delete_permission = providers.Factory(
        DeletePermissionUseCase, rdbms_uow=db.container.uow
    )

    get_role_by_id = providers.Factory(
        GetRoleByIdUseCase, rdbms_uow=db.container.uow
    )

    get_all_roles = providers.Factory(
        GetAllRolesUseCase, rdbms_uow=db.container.uow
    )

    create_role = providers.Factory(
        CreateRoleUseCase, rdbms_uow=db.container.uow
    )

    update_role = providers.Factory(
        UpdateRoleUseCase, rdbms_uow=db.container.uow
    )

    delete_role = providers.Factory(
        DeleteRoleUseCase, rdbms_uow=db.container.uow
    )

    attach_permission_to_role = providers.Factory(
        AttachPermissionToRoleUseCase, rdbms_uow=db.container.uow
    )

    detach_role_with_permission = providers.Factory(
        DetachRoleWithPermissionUseCase, rdbms_uow=db.container.uow
    )

    get_list_of_users = providers.Factory(
        ListUsersUseCase, rdbms_uow=db.container.uow
    )

    update_profile = providers.Factory(
        UpdateProfileUseCase, rdbms_uow=db.container.uow
    )

    delete_profile = providers.Factory(
        DeleteProfileUseCase, rdbms_uow=db.container.uow
    )

    login_user = providers.Factory(
        LoginUseCase,
        rdbms_uow=db.container.uow,
        jwt_encoder=jwt_encoder,
        password_cryptografer=password_cryptografer,
    )

    refresh_token = providers.Factory(
        RefreshTokenUseCase,
        rdbms_uow=db.container.uow,
        jwt_encoder=jwt_encoder,
    )

    get_current_user = providers.Factory(
        GetCurrentUserUseCase,
        rdbms_uow=db.container.uow,
        jwt_encoder=jwt_encoder,
    )
