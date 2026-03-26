from httpx import AsyncClient


class TestGet:

    async def test_case_1(
        self,
        client: AsyncClient, url_get_permission: str, regular_permission_id: str
    ) -> None:
            url = url_get_permission.format(permission_id=regular_permission_id)
            response = await client.get(url)

            assert response.status_code == 200
            assert response.json()['id'] == str(regular_permission_id)

    async def test_case_2(
        self,
        client: AsyncClient, url_get_permission: str, foreign_permission_id: str
    ) -> None:
            url = url_get_permission.format(permission_id=foreign_permission_id)
            response = await client.get(url)

            assert response.status_code == 400

    async def test_case_3(
        self,
        client: AsyncClient,
        url_permission: str,
        regular_permission_id: str,
        foreign_permission_id: str,
    ) -> None:
            response = await client.get(url_permission)

            assert response.status_code == 200
            assert len(response.json()) == 1
