from internal import model


class WGService(model.IWGService):
    def __init__(self, wg_repo: model.IWGRepository):
        self.wg_repo = wg_repo

    async def create_client(self, client_address: str) -> str:
        return await self.wg_repo.create_client(client_address)

    async def delete_client(self, client_address: str):
        await self.wg_repo.delete_client(client_address)

    async def client_by_address(self, client_address: str) -> list[model.Client]:
        return await self.wg_repo.client_by_address(client_address)

    async def get_config(self, wg_client_id) -> bytes:
        return await self.wg_repo.get_config(wg_client_id)
