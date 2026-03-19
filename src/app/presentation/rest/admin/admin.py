from sqladmin import ModelView
from src.app.infra.connection_engines.sqla.models.user import User
from src.app.infra.connection_engines.sqla.models.role import Role
from src.app.infra.connection_engines.sqla.models.permission import Permission


class UserAdmin(ModelView, model=User):

    column_list = [
        User.id,
        User.email,
        User.first_name,
        User.last_name,
        User.role,
        User.is_active,
        User.created_at
    ]
    column_searchable_list = [User.email, User.last_name]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Accounts"

class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name, Role.permissions]
    form_columns = [Role.name, Role.description, Role.permissions]
    name = "Роль"
    name_plural = "Роли"
    icon = "fa-solid fa-users-gear"
    category = "Permissions"

class PermissionAdmin(ModelView, model=Permission):
    column_list = [Permission.id, Permission.name, Permission.description]
    column_searchable_list = [Permission.name]
    name = "Разрешение"
    name_plural = "Разрешения"
    icon = "fa-solid fa-key"
    category = "Permissions"