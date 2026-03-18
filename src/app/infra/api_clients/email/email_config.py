from typing import cast

from fastapi_mail import ConnectionConfig
from pydantic import EmailStr

from src.app.config import Config


def provide_mail_config(config: Config) -> ConnectionConfig:
    return ConnectionConfig(
        MAIL_USERNAME=config.MAIL.username,
        MAIL_PASSWORD=config.MAIL.password,
        MAIL_FROM=cast(EmailStr, config.MAIL.mail_from),
        MAIL_FROM_NAME=config.MAIL.mail_from_name,
        MAIL_SERVER=config.MAIL.server,
        MAIL_PORT=config.MAIL.port,
        MAIL_STARTTLS=config.MAIL.starttls,
        MAIL_SSL_TLS=config.MAIL.ssl_tls,
        TEMPLATE_FOLDER=config.MAIL.path_templates,
    )
