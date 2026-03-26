from httpx import AsyncClient


class TestMe:

    async def test_case_1(
        self,
        client: AsyncClient,
        login_payload_of_regular_user: dict[str, str],
        url_login_user: str,
        url_auth_me: str,
    ) -> None:
            login_response = await client.post(
                url_login_user, json=login_payload_of_regular_user
            )

            response = await client.get(
                url_auth_me,
                params={"token": login_response.json()["access_token"]},
            )

            assert response.status_code == 200
            assert response.json()["email"] == login_payload_of_regular_user["email"]

    async def test_case_2(
        self,
        client: AsyncClient,
        url_auth_me: str,
    ) -> None:
            response = await client.get(
                url_auth_me,
                params={"token": "invalid-token"},
            )

            assert response.status_code == 400
