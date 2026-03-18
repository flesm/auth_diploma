from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.app.application.entities.user import UserEntity
from src.app.infra.connection_engines.sqla.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, server_default=text('true'))
    is_verified = Column(Boolean, server_default=text('false'))
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    role = relationship("Role", lazy="selectin")

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_verified=self.is_verified,
            role_id=self.role_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
