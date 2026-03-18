import pytest


@pytest.fixture
def url_role_permission(url_v1: str) -> str:
    return f"{url_v1}/role_permission"
