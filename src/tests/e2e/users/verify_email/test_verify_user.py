from httpx import AsyncClient


async def test_verify_regular_user_success(
    client: AsyncClient,
    url_verify_email: str,
    verify_token_of_unverified_user: str,
) -> None:

    response = await client.get(
        url_verify_email, params={"token": verify_token_of_unverified_user}
    )
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["message"] == "User successfully verified"


async def test_verify_already_verified_forbidden(
    client: AsyncClient,
    url_verify_email: str,
    verify_token_of_verified_user: str,
) -> None:

    response = await client.get(
        url_verify_email, params={"token": verify_token_of_verified_user}
    )
    response_json = response.json()
    assert response.status_code == 409
    assert response_json["detail"] == "User already verified."
