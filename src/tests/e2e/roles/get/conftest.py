import pytest


@pytest.fixture
def url_get_role(url_role: str) -> str:
    return f"{url_role}/{{role_id}}"
