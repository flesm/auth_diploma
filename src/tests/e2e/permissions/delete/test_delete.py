from httpx import AsyncClient


class TestDelete:

    async def test_case_1(
        self,
        client: AsyncClient, url_permission: str, regular_permission_id: str
    ) -> None:
            response = await client.delete(
                url_permission, params={"permission_id": regular_permission_id}
            )

            assert response.status_code == 200

    async def test_case_2(
        self,
        client: AsyncClient, url_permission: str, foreign_permission_id: str
    ) -> None:
            response = await client.delete(
                url_permission, params={"permission_id": foreign_permission_id}
            )

            assert response.status_code == 400
