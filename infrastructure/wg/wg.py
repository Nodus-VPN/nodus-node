import aiohttp
from internal import model


class WG(model.WGInterface):
    def __init__(self, host, port):
        self.base_url = f"http://{host}:{port}/api"

    async def __async_get(self, path: str, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=None, cookies=cookies) as session:
            async with session.get(self.base_url + path, headers=headers) as resp:
                return resp

    async def __async_post(self, path: str, body: dict, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            async with session.post(self.base_url + path, json=body, headers=headers) as resp:
                return await resp.json()

    async def __async_delete(self, path: str, body: dict = None, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            async with session.delete(self.base_url + path, json=body, headers=headers) as resp:
                return await resp.json()

    async def create_client(self, client_address: str) -> bool:
        response = await self.__async_post("/wireguard/client", {"name": client_address})
        return response["success"]

    async def get_config(self, wg_client_id: str):
        response = await self.__async_get(f"/wireguard/client/{wg_client_id}/configuration")
        return response

    async def delete_client(self, client_wg_id: str) -> None:
        response = await self.__async_delete(f"/wireguard/client/{client_wg_id}")
        return response["success"]

    async def all_client(self) -> list[model.WGClient]:
        response = await self.__async_get("/wireguard/client")
        response = await response.json()
        print(response)
        for i in range(len(response)):
            response[i] = model.WGClient(**response[i])
        return response

    async def client_by_address(self, client_address: str) -> model.WGClient:
        all_clients = await self.all_client()
        print(all_clients)
        for client in all_clients:
            if client.name == client_address:
                return client
