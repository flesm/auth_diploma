from httpx import AsyncClient


async def test_detach_permission_with_role_success(
    client: AsyncClient,
    url_role_permission_detach: str,
    attached_permission_ro_role: None,
    another_regular_role_id: str,
    another_regular_permission_id: str,
) -> None:
    url = url_role_permission_detach.format(
        role_id=another_regular_role_id,
        permission_id=another_regular_permission_id,
    )
    response = await client.delete(url)
    assert response.status_code == 200


async def test_detach_role_with_permission_not_found(
    client: AsyncClient,
    url_role_permission_detach: str,
    attached_permission_ro_role: None,
    another_regular_role_id: str,
    foreign_permission_id: str,
) -> None:
    url = url_role_permission_detach.format(
        role_id=another_regular_role_id,
        permission_id=foreign_permission_id,
    )
    response = await client.delete(url)
    assert response.status_code == 400
