from sqlalchemy import Column, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.app.application.entities.role import RoleEntity
from src.app.infra.connection_engines.sqla.models.base import Base
from src.app.infra.connection_engines.sqla.models.role_permission import (
    role_permissions,
)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    permissions = relationship(
        "Permission",
        secondary=role_permissions,
        back_populates="roles",
        lazy="selectin",
    )

    def to_entity(self) -> RoleEntity:
        return RoleEntity(
            id=self.id,
            name=self.name,
            description=self.description,
            permissions=[
                permission.to_entity() for permission in self.permissions
            ],
        )
