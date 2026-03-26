import pytest


@pytest.fixture
def url_refresh_token(url_auth: str) -> str:
    return f"{url_auth}/token/refresh"
