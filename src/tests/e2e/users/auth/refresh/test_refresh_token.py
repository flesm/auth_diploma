from httpx import AsyncClient


class TestRefreshToken:

    async def test_case_1(
        self,
        client: AsyncClient,
        login_payload_of_regular_user: dict[str, str],
        url_login_user: str,
        url_refresh_token: str,
    ) -> None:
            login_response = await client.post(
                url_login_user, json=login_payload_of_regular_user
            )

            refresh_response = await client.post(
                url_refresh_token,
                params={"token": login_response.json()["refresh_token"]},
            )

            assert refresh_response.status_code == 200
            assert isinstance(refresh_response.json(), str)

    async def test_case_2(
        self,
        client: AsyncClient,
        url_refresh_token: str,
    ) -> None:
            response = await client.post(
                url_refresh_token,
                params={"token": "invalid-token"},
            )

            assert response.status_code == 400
