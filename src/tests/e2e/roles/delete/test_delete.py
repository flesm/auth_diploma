from httpx import AsyncClient


async def test_delete_regular_role_success(
    client: AsyncClient, url_role: str, regular_role_id: str
) -> None:
    response = await client.delete(
        url_role, params={"role_id": regular_role_id}
    )

    assert response.status_code == 200


async def test_delete_role_not_found(
    client: AsyncClient, url_role: str, foreign_role_id: str
) -> None:
    response = await client.delete(
        url_role, params={"role_id": foreign_role_id}
    )

    assert response.status_code == 400
