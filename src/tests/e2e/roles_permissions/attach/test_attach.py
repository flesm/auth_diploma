from httpx import AsyncClient


class TestAttach:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_role_permission_attach: str,
        another_regular_role_id: str,
        another_regular_permission_id: str,
    ) -> None:
            url = url_role_permission_attach.format(
                role_id=another_regular_role_id,
                permission_id=another_regular_permission_id,
            )
            response = await client.post(url)
            assert response.status_code == 200

    async def test_case_2(
        self,
        client: AsyncClient,
        url_role_permission_attach: str,
        foreign_role_id: str,
        another_regular_permission_id: str,
    ) -> None:
            url = url_role_permission_attach.format(
                role_id=foreign_role_id,
                permission_id=another_regular_permission_id,
            )
            response = await client.post(url)
            assert response.status_code == 400
