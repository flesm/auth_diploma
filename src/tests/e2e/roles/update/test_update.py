from httpx import AsyncClient


async def test_update_role_success(
    client: AsyncClient,
    url_role: str,
    payload_update_regular_role: dict[str, str],
    regular_role_id: str,
) -> None:
    response = await client.patch(
        url_role,
        params={'role_id': regular_role_id},
        json=payload_update_regular_role,
    )

    assert response.status_code == 200
    assert response.json()['name'] == payload_update_regular_role['name']


async def test_update_role_already_exist(
    client: AsyncClient,
    url_role: str,
    regular_role_id: str,
    another_regular_role_id: str,
    payload_update_existed_regular_role: dict[str, str],
) -> None:

    response = await client.patch(
        url_role,
        params={'role_id': regular_role_id},
        json=payload_update_existed_regular_role,
    )
    assert response.status_code == 400


async def test_update_role_not_found(
    client: AsyncClient,
    url_role: str,
    foreign_role_id: str,
    payload_update_existed_regular_role: dict[str, str],
) -> None:

    response = await client.patch(
        url_role,
        params={'role_id': foreign_role_id},
        json=payload_update_existed_regular_role,
    )
    assert response.status_code == 400
