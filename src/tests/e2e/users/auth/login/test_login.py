from httpx import AsyncClient


async def test_login_regular_user_success(
    client: AsyncClient,
    login_payload_of_regular_user: dict[str, str],
    url_login_user: str,
) -> None:

    response = await client.post(
        url_login_user, json=login_payload_of_regular_user
    )

    assert response.status_code == 200
    assert response.json()['token_type'] == 'bearer'


async def test_login_foreign_user_(
    client: AsyncClient,
    login_payload_of_foreign_user: dict[str, str],
    url_login_user: str,
) -> None:

    response = await client.post(
        url_login_user, json=login_payload_of_foreign_user
    )

    assert response.status_code == 400
