import asyncio
import uuid
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.app.infra.connection_engines.sqla.db import Database
from src.app.infra.connection_engines.sqla.models.user import User
from src.app.infra.connection_engines.sqla.models.role import Role
from src.app.infra.connection_engines.sqla.models.permission import Permission
from src.app.infra.crypto.password_cryptografer import CCPasswordCryptografer
from src.app.config import Config


async def seed_data():
    config = Config()
    db = Database(config.DB)
    crypto = CCPasswordCryptografer()

    async with db.session_factory() as session:

        """Seed permissions"""
        permissions_data = {
            "user:read": "Просмотр пользователей",
            "user:write": "Редактирование пользователей",
            "admin:all": "Полный доступ к системе",
            "content:read": "Просмотр учебных материалов",
            "content:write": "Создание и проверка заданий",
        }

        db_permissions = {}
        for name, desc in permissions_data.items():
            stmt = select(Permission).where(Permission.name == name)
            res = (await session.execute(stmt)).scalar_one_or_none()
            if not res:
                res = Permission(id=uuid.uuid4(), name=name, description=desc)
                session.add(res)
            db_permissions[name] = res

        await session.flush()

        """Seed roles"""
        roles_definitions = {
            "admin": [db_permissions["admin:all"]],
            "mentor": [db_permissions["user:read"], db_permissions["content:read"], db_permissions["content:write"]],
            "intern": [db_permissions["content:read"]]
        }

        db_roles = {}
        for role_name, perms in roles_definitions.items():
            stmt = select(Role).where(Role.name == role_name).options(selectinload(Role.permissions))
            role_obj = (await session.execute(stmt)).scalar_one_or_none()

            if not role_obj:
                role_obj = Role(
                    id=uuid.uuid4(),
                    name=role_name,
                    permissions=perms
                )
                session.add(role_obj)
            db_roles[role_name] = role_obj

        await session.flush()

        users_to_create = [
            {
                "email": "admin@example.com",
                "password": "admin12345",
                "first_name": "Admin",
                "last_name": "System",
                "role": db_roles["admin"],
            },
            {
                "email": "mentor@example.com",
                "password": "mentor12345",
                "first_name": "Ivan",
                "last_name": "Mentor",
                "role": db_roles["mentor"],
            },
            {
                "email": "intern@example.com",
                "password": "intern12345",
                "first_name": "Petr",
                "last_name": "Intern",
                "role": db_roles["intern"],
            }
        ]

        for u_data in users_to_create:
            stmt_user = select(User).where(User.email == u_data["email"])
            existing_user = (await session.execute(stmt_user)).scalar_one_or_none()

            if not existing_user:
                new_user = User(
                    id=uuid.uuid4(),
                    email=u_data["email"],
                    hashed_password=crypto.hash(u_data["password"]),
                    first_name=u_data["first_name"],
                    last_name=u_data["last_name"],
                    role_id=u_data["role"].id,
                    is_active=True,
                    is_verified=True
                )
                session.add(new_user)
                print(f"Создан пользователь: {u_data['email']} ({u_data['role'].name})")

        await session.commit()
        print("База успешно заполнена начальными данными!")


if __name__ == "__main__":
    asyncio.run(seed_data())