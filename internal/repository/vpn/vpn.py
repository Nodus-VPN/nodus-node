from internal import model


class VPNRepository(model.IVPNRepository):
    def __init__(self, db: model.DBInterface, wg: model.WGInterface, ovpn: model.OVPNInterface):
        self.db = db
        self.wg = wg
        self.ovpn = ovpn

    async def create_wg_client(self, client_address: str) -> str:
        await self.wg.create_client(client_address)
        client = await self.wg.client_by_address(client_address)

        query_params = {"client_address": client_address, "client_wg_id": client.id}
        await self.db.insert(model.create_wg_client, query_params)
        return client.id

    async def set_wg_client(self, client_address: str) -> str:
        await self.wg.create_client(client_address)
        client = await self.wg.client_by_address(client_address)

        query_params = {"client_address": client_address, "client_wg_id": client.id}
        await self.db.insert(model.set_wg_client, query_params)
        return client.id

    async def get_wg_config(self, wg_client_id: str) -> bytes:
        return await self.wg.get_config(wg_client_id)

    # OPENVPN
    async def create_ovpn_client(self, client_address: str):
        await self.ovpn.create_client(client_address)

        query_params = {"client_address": client_address, "client_ovpn_id": client_address}
        await self.db.insert(model.create_wg_client, query_params)

    async def set_ovpn_client(self, client_address: str):
        self.ovpn.create_client(client_address)

        query_params = {"client_address": client_address, "client_ovpn_id": client_address}
        await self.db.insert(model.set_ovpn_client, query_params)

    # GENERAL
    async def get_ovpn_config(self, client_address: str) -> bytes:
        return self.ovpn.get_config(client_address)

    async def client_by_address(self, client_address: str) -> list[model.NodeClient]:
        query_params = {"client_address": client_address}
        rows = await self.db.select(model.client_by_address, query_params)

        if rows:
            rows = model.NodeClient.serialize(rows)
        return rows

    async def delete_client(self, client_address: str):
        try:
            client = await self.wg.client_by_address(client_address)
            await self.wg.delete_client(client.id)
        except:
            pass

        try:
            self.ovpn.delete_client(client_address)
        except:
            pass

        query_params = {"client_address": client_address}
        await self.db.delete(model.delete_client_query, query_params)
