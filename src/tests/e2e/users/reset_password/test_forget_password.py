from httpx import AsyncClient


async def test_forget_password_regular_user_success(
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
