from sqlalchemy import Column, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.app.application.entities.permission import PermissionEntity
from src.app.infra.connection_engines.sqla.models.base import Base
from src.app.infra.connection_engines.sqla.models.role_permission import (
    role_permissions,
)


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    roles = relationship(
        "Role",
        secondary=role_permissions,
        back_populates="permissions",
        lazy="selectin",
    )

    def to_entity(self) -> PermissionEntity:
        return PermissionEntity(
            id=self.id, name=self.name, description=self.description
        )
