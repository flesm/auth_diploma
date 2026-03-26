from httpx import AsyncClient


class TestResendVerification:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_resend_verification: str,
        unverified_regular_user: str,
    ) -> None:

            response = await client.post(
                url_resend_verification, params={"email": unverified_regular_user}
            )
            response_json = response.json()
            assert response.status_code == 200
            assert response_json["message"] == "Verification successfully resend"

    async def test_case_2(
        self,
        client: AsyncClient,
        url_resend_verification: str,
        verified_regular_user: str,
    ) -> None:

            response = await client.post(
                url_resend_verification, params={"email": verified_regular_user}
            )
            response_json = response.json()
            assert response.status_code == 409
            assert response_json["detail"] == "User already verified."
