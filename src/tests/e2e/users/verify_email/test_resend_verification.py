from httpx import AsyncClient


async def test_resend_verification_to_regular_user_success(
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


async def test_resend_verification_to_already_verified_forbidden(
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
