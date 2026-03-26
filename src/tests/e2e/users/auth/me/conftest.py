import pytest


@pytest.fixture
def url_auth_me(url_auth: str) -> str:
    return f"{url_auth}/me"
