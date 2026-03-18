from uuid import UUID

from httpx import AsyncClient


async def test_delete_profile_common_user_success(
    client: AsyncClient,
    url_profile: str,
    common_user_id: UUID,
) -> None:
    response = await client.delete(
        url_profile,
        params={'user_id': str(common_user_id)},
    )

    assert response.status_code == 200


async def test_delete_profile_foreign_user_not_found(
    client: AsyncClient,
    url_profile: str,
    foreign_user_id: UUID,
) -> None:
    response = await client.delete(
        url_profile,
        params={'user_id': str(foreign_user_id)},
    )

    assert response.status_code == 404
