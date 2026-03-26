from httpx import AsyncClient


class TestForgetPassword:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_forget_password: str,
        unverified_regular_user: str,
    ) -> None:

            response = await client.post(
                url_forget_password, params={"email": unverified_regular_user}
            )
            response_json = response.json()
            assert response.status_code == 200
            assert response_json["message"] == "Reset link has been sent"
