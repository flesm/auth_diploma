from uuid import UUID

from httpx import AsyncClient


class TestRegisterUser:

    async def test_case_1(
        self,
        client: AsyncClient,
        payload_register_regular_user: dict[str, str],
        url_register_user: str,
    ) -> None:

            response = await client.post(
                url_register_user, json=payload_register_regular_user
            )

            assert response.status_code == 200

            response_json = response.json()

            expected_response = {
                "id": str(UUID(response_json["id"])),
                "email": payload_register_regular_user["email"],
                "first_name": payload_register_regular_user["first_name"],
                "last_name": payload_register_regular_user["last_name"],
                "role_id": str(UUID(response_json["role_id"])),
                "is_active": True,
                "is_verified": False,
            }

            for key, value in expected_response.items():
                assert response_json[key] == value

    async def test_case_2(
        self,
        client: AsyncClient,
        payload_register_regular_user: dict[str, str],
        url_register_user: str,
    ) -> None:

            await client.post(url_register_user, json=payload_register_regular_user)
            response = await client.post(
                url_register_user, json=payload_register_regular_user
            )
            response_json = response.json()

            assert response.status_code == 409
            assert response_json["detail"] == "Email already registered."
