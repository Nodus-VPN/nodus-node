import aiohttp
from internal import model


class WG(model.WGInterface):
    def __init__(self, host):
        self.base_url = f"http://{host}/api"

    async def __async_get(self, path: str, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=None, cookies=cookies) as session:
            async with session.get(self.base_url + path, headers=headers) as resp:
                return await resp.json()

    async def __async_post(self, path: str, body: dict, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            async with session.post(self.base_url + path, json=body, headers=headers) as resp:
                return await resp.json()

    async def create_client(self, client_address: str) -> bool:
        response = await self.__async_post("/wireguard/client", {"name": client_address})
        return response["success"]

    async def delete_client(self, client_wg_id: str) -> None:
        pass

    async def all_client(self) -> list[model.WGClient]:
        response = await self.__async_get("/wireguard/client")
        for i in range(len(response)):
            response[i] = model.WGClient(**response[i])
        return response

    async def client_by_address(self, client_address: str) -> model.WGClient:
        all_clients = await self.all_client()
        for client in all_clients:
            if client.address == client_address:
                return client
