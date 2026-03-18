from pydantic import EmailStr, PostgresDsn, SecretStr

from src.app.config import AppConfig, Config, DBConfig, JWTConfig, MailConfig


class FakeDBConfig(DBConfig):
    host: str
    port: int
    db: str
    user: str
    password: SecretStr
    dsn: PostgresDsn


class FakeJWTConfig(JWTConfig):
    expire_minutes: int
    access_expire_minutes: int
    refresh_expire_minutes: int

    forget_pwd_secret_key: str
    verify_email_secret_key: str
    access_secret_key: str
    refresh_secret_key: str

    algorithm: str


class FakeAppConfig(AppConfig):
    host: str


class FakeMailConfig(MailConfig):
    username: str
    password: SecretStr
    mail_from: EmailStr
    mail_from_name: str
    server: str
    port: int
    starttls: bool
    ssl_tls: bool
    path_templates: str


class FakeConfig(Config):
    class Config:
        env_file = "/home/young/stajka/auth/.env.test"
        env_nested_delimiter = "__"

    DB: FakeDBConfig
    JWT: FakeJWTConfig
    APP: FakeAppConfig
    MAIL: FakeMailConfig
