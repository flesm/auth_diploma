from httpx import AsyncClient


class TestCreate:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_permission: str,
        payload_create_regular_permission: dict[str, str],
    ) -> None:
            response = await client.post(
                url_permission, json=payload_create_regular_permission
            )

            assert response.status_code == 200
            assert response.json()['name'] == payload_create_regular_permission['name']

    async def test_case_2(
        self,
        client: AsyncClient,
        url_permission: str,
        payload_create_regular_permission: dict[str, str],
    ) -> None:
            await client.post(url_permission, json=payload_create_regular_permission)

            response = await client.post(
                url_permission, json=payload_create_regular_permission
            )

            assert response.status_code == 400
