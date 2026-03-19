from fastapi import FastAPI
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine
from src.app.presentation.rest.admin.admin import UserAdmin, RoleAdmin, PermissionAdmin


def setup_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(
        app,
        engine,
        title="Auth Service Admin",
        base_url="/admin"
    )

    admin.add_view(UserAdmin)
    admin.add_view(RoleAdmin)
    admin.add_view(PermissionAdmin)

    return admin