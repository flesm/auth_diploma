import pytest


@pytest.fixture
def url_role_permission_attach(url_role_permission: str) -> str:
    return (
        f"{url_role_permission}/role/{{role_id}}/permission/{{permission_id}}"
    )
