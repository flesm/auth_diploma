from httpx import AsyncClient


async def test_get_role_by_id_success(
    client: AsyncClient, url_get_role: str, regular_role_id: str
) -> None:
    url = url_get_role.format(role_id=regular_role_id)
    response = await client.get(url)

    assert response.status_code == 200
    assert response.json()['id'] == str(regular_role_id)


async def test_get_role_by_id_not_found(
    client: AsyncClient, url_get_role: str, foreign_role_id: str
) -> None:
    url = url_get_role.format(role_id=foreign_role_id)
    response = await client.get(url)

    assert response.status_code == 400


async def test_get_all_roles_success(
    client: AsyncClient,
    url_role: str,
    regular_role_id: str,
    foreign_role_id: str,
) -> None:
    response = await client.get(url_role)

    assert response.status_code == 200
