from httpx import AsyncClient


async def test_get_list_of_users_success(
    client: AsyncClient,
    url_profile: str,
    verified_regular_user: str,
    unverified_regular_user: str,
) -> None:

    response = await client.get(url_profile)
    assert response.status_code == 200
    assert len(response.json()) == 2


async def test_get_list_of_users_with_offset_success(
    client: AsyncClient,
    url_profile: str,
    verified_regular_user: str,
    unverified_regular_user: str,
) -> None:

    response = await client.get(url_profile, params={"offset": 1})
    assert response.status_code == 200
    assert len(response.json()) == 1


async def test_get_list_of_users_with_limit_success(
    client: AsyncClient,
    url_profile: str,
    verified_regular_user: str,
    unverified_regular_user: str,
) -> None:

    response = await client.get(url_profile, params={"limit": 1})
    assert response.status_code == 200
    assert len(response.json()) == 1
