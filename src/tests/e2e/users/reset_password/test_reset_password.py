from httpx import AsyncClient


class TestResetPassword:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_reset_password: str,
        payload_reset_password_regular_user: dict[str, str],
    ) -> None:

            response = await client.post(
                url_reset_password, json=payload_reset_password_regular_user
            )
            response_json = response.json()
            assert response.status_code == 200
            assert response_json["message"] == "Password has been successfully reseted"

    async def test_case_2(
        self,
        client: AsyncClient,
        url_reset_password: str,
        payload_reset_password_invalid_reset_link: dict[str, str],
    ) -> None:

            response = await client.post(
                url_reset_password, json=payload_reset_password_invalid_reset_link
            )
            response_json = response.json()
            assert response.status_code == 400
            assert response_json["detail"] == "Invalid or expired reset link."
