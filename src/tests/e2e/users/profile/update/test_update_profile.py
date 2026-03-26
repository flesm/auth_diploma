from uuid import UUID

from httpx import AsyncClient


class TestUpdateProfile:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_profile: str,
        payload_for_update_common_user_profile: dict[str, str],
        common_user_id: UUID,
    ) -> None:
            response = await client.patch(
                url_profile,
                params={'user_id': str(common_user_id)},
                json=payload_for_update_common_user_profile,
            )

            assert response.status_code == 200
            assert (
                response.json()['first_name']
                == payload_for_update_common_user_profile['first_name']
            )

    async def test_case_2(
        self,
        client: AsyncClient,
        url_profile: str,
        payload_for_update_common_user_profile: dict[str, str],
        foreign_user_id: UUID,
    ) -> None:
            response = await client.patch(
                url_profile,
                params={'user_id': str(foreign_user_id)},
                json=payload_for_update_common_user_profile,
            )

            assert response.status_code == 404
