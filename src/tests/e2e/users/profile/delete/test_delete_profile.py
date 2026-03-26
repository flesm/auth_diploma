from uuid import UUID

from httpx import AsyncClient


class TestDeleteProfile:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_profile: str,
        common_user_id: UUID,
    ) -> None:
            response = await client.delete(
                url_profile,
                params={'user_id': str(common_user_id)},
            )

            assert response.status_code == 200

    async def test_case_2(
        self,
        client: AsyncClient,
        url_profile: str,
        foreign_user_id: UUID,
    ) -> None:
            response = await client.delete(
                url_profile,
                params={'user_id': str(foreign_user_id)},
            )

            assert response.status_code == 404
