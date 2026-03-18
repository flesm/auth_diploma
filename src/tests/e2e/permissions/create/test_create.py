from httpx import AsyncClient


async def test_create_permission_success(
    client: AsyncClient,
    url_permission: str,
    payload_create_regular_permission: dict[str, str],
) -> None:
    response = await client.post(
        url_permission, json=payload_create_regular_permission
    )

    assert response.status_code == 200
    assert response.json()['name'] == payload_create_regular_permission['name']


async def test_create_permission_already_exist(
    client: AsyncClient,
    url_permission: str,
    payload_create_regular_permission: dict[str, str],
) -> None:
    await client.post(url_permission, json=payload_create_regular_permission)

    response = await client.post(
        url_permission, json=payload_create_regular_permission
    )

    assert response.status_code == 400
