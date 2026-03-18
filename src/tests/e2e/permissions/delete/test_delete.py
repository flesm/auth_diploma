from httpx import AsyncClient


async def test_delete_regular_permission_success(
    client: AsyncClient, url_permission: str, regular_permission_id: str
) -> None:
    response = await client.delete(
        url_permission, params={"permission_id": regular_permission_id}
    )

    assert response.status_code == 200


async def test_delete_permission_not_found(
    client: AsyncClient, url_permission: str, foreign_permission_id: str
) -> None:
    response = await client.delete(
        url_permission, params={"permission_id": foreign_permission_id}
    )

    assert response.status_code == 400
