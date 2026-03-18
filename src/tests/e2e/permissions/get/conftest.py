import pytest


@pytest.fixture
def url_get_permission(url_permission: str) -> str:
    return f"{url_permission}/{{permission_id}}"
