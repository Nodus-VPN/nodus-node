from internal import model
import aiohttp


class WGClient(model.IWGClient):
    def __init__(self, host, port):
        self.base_url = f"http://{host}:{port}/api/auth"

    async def __async_get(self, path: str, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=None, cookies=cookies) as session:
            async with session.get(self.base_url + path, headers=headers) as resp:
                return await resp.json()

    async def __async_post(self, path: str, body: dict, headers: dict = None, cookies: dict = None):
        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            async with session.post(self.base_url + path, json=body, headers=headers) as resp:
                return await resp.json()

    async def create_client(self):
        pass

    async def delete_client(self):
        pass

    async def all_client(self):
        pass
