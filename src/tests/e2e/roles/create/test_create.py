from httpx import AsyncClient


class TestCreate:

    async def test_case_1(
        self,
        client: AsyncClient,
        url_role: str,
        payload_create_regular_role: dict[str, str],
    ) -> None:
            response = await client.post(url_role, json=payload_create_regular_role)

            assert response.status_code == 200
            assert response.json()['name'] == payload_create_regular_role['name']

    async def test_case_2(
        self,
        client: AsyncClient,
        url_role: str,
        payload_create_regular_role: dict[str, str],
    ) -> None:
            await client.post(url_role, json=payload_create_regular_role)

            response = await client.post(url_role, json=payload_create_regular_role)

            assert response.status_code == 400
