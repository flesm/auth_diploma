from httpx import AsyncClient


class TestGetListOfUsers:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_profile: str,
        verified_regular_user: str,
        unverified_regular_user: str,
    ) -> None:

            response = await client.get(url_profile)
            assert response.status_code == 200
            assert len(response.json()) == 2

    async def test_case_2(
        self,
        client: AsyncClient,
        url_profile: str,
        verified_regular_user: str,
        unverified_regular_user: str,
    ) -> None:

            response = await client.get(url_profile, params={"offset": 1})
            assert response.status_code == 200
            assert len(response.json()) == 1

    async def test_case_3(
        self,
        client: AsyncClient,
        url_profile: str,
        verified_regular_user: str,
        unverified_regular_user: str,
    ) -> None:

            response = await client.get(url_profile, params={"limit": 1})
            assert response.status_code == 200
            assert len(response.json()) == 1
