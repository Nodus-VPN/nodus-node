from internal import model


class WGRepository(model.IWGRepository):
    def __init__(self, db: model.DBInterface, wg: model.WGInterface):
        self.db = db
        self.wg = wg

    async def create_client(self, client_address: str) -> str:
        await self.wg.create_client(client_address)
        client = await self.wg.client_by_address(client_address)

        query_params = {"client_address": client_address, "client_wg_id": client.id}
        await self.db.insert(model.create_wg_client, query_params)
        return client.id

    async def delete_client(self, client_address: str):
        client = await self.wg.client_by_address(client_address)
        await self.wg.delete_client(client.id)

        query_params = {"client_wg_id": client.id}
        await self.db.delete(model.delete_wg_client_query, query_params)

    async def client_by_address(self, client_address: str) -> list[model.Client]:
        query_params = {"client_address": client_address}
        rows = await self.db.select(model.client_by_address, query_params)

        if rows:
            rows = model.Client.serialize(rows)
        return rows

    async def get_config(self, wg_client_id) -> bytes:
        return await self.wg.get_config(wg_client_id)
