import pytest


@pytest.fixture
def payload_for_update_common_user_profile() -> dict[str, str]:
    return {
        "first_name": "John",
        "last_name": "Bell",
        "role_id": "8fa85f64-5717-4562-b3fc-2c963f66afa6",
    }
