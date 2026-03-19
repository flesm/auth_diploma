from pydantic import BaseModel, EmailStr, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings


class DBConfig(BaseModel):
    host: str
    port: int
    db: str
    user: str
    password: SecretStr
    dsn: PostgresDsn


class JWTConfig(BaseModel):
    expire_minutes: int
    access_expire_minutes: int
    refresh_expire_minutes: int

    forget_pwd_secret_key: str
    verify_email_secret_key: str
    access_secret_key: str
    refresh_secret_key: str

    algorithm: str


class AppConfig(BaseModel):
    host: str


class MailConfig(BaseModel):
    username: str
    password: SecretStr
    mail_from: EmailStr
    mail_from_name: str
    server: str
    port: int
    starttls: bool
    ssl_tls: bool
    path_templates: str


class Config(BaseSettings):
    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"
        extra = "ignore"

    DB: DBConfig
    JWT: JWTConfig
    APP: AppConfig
    MAIL: MailConfig
