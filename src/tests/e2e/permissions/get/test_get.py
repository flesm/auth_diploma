from httpx import AsyncClient


async def test_get_permission_by_id_success(
    client: AsyncClient, url_get_permission: str, regular_permission_id: str
) -> None:
    url = url_get_permission.format(permission_id=regular_permission_id)
    response = await client.get(url)

    assert response.status_code == 200
    assert response.json()['id'] == str(regular_permission_id)


async def test_get_permission_by_id_not_found(
    client: AsyncClient, url_get_permission: str, foreign_permission_id: str
) -> None:
    url = url_get_permission.format(permission_id=foreign_permission_id)
    response = await client.get(url)

    assert response.status_code == 400


async def test_get_all_permissions_success(
    client: AsyncClient,
    url_permission: str,
    regular_permission_id: str,
    foreign_permission_id: str,
) -> None:
    response = await client.get(url_permission)

    assert response.status_code == 200
    assert len(response.json()) == 1
