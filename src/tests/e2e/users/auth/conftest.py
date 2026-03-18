import pytest


@pytest.fixture
def url_auth(url_v1: str) -> str:
    return f"{url_v1}/auth"
