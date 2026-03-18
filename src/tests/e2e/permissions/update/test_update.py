from httpx import AsyncClient


async def test_update_permission_success(
    client: AsyncClient,
    url_permission: str,
    payload_update_regular_permission: dict[str, str],
    regular_permission_id: str,
) -> None:
    response = await client.patch(
        url_permission,
        params={'permission_id': regular_permission_id},
        json=payload_update_regular_permission,
    )

    assert response.status_code == 200
    assert response.json()['name'] == payload_update_regular_permission['name']


async def test_update_permission_already_exist(
    client: AsyncClient,
    url_permission: str,
    regular_permission_id: str,
    another_regular_permission_id: str,
    payload_update_existed_regular_permission: dict[str, str],
) -> None:

    response = await client.patch(
        url_permission,
        params={'permission_id': regular_permission_id},
        json=payload_update_existed_regular_permission,
    )
    assert response.status_code == 400


async def test_update_permission_not_found(
    client: AsyncClient,
    url_permission: str,
    foreign_permission_id: str,
    payload_update_existed_regular_permission: dict[str, str],
) -> None:

    response = await client.patch(
        url_permission,
        params={'permission_id': foreign_permission_id},
        json=payload_update_existed_regular_permission,
    )
    assert response.status_code == 400
