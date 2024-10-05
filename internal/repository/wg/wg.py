from internal import model


class WGRepository(model.IWGRepository):
    def __init__(self, db: model.DBInterface, wg: model.WGInterface):
        self.db = db
        self.wg = wg

    async def create_client(self, client_address: str):
        success = await self.wg.create_client(client_address)
        if not success:
            raise Exception(f'Failed to create client {client_address}')

        client = await self.wg.client_by_address(client_address)

        query_params = {"client_address": client_address, "client_wg_id": client.id}
        await self.db.insert(model.create_wg_client, query_params)
