from internal import model


class VPNService(model.IVPNService):
    def __init__(self, vpn_repo: model.IVPNRepository):
        self.vpn_repo = vpn_repo

    # WIREGUARD
    async def create_wg_client(self, client_address: str) -> str:
        return await self.vpn_repo.create_wg_client(client_address)

    async def set_wg_client(self, client_address: str) -> str:
        return await self.vpn_repo.set_wg_client(client_address)

    async def get_wg_config(self, wg_client_id: str) -> bytes:
        return await self.vpn_repo.get_wg_config(wg_client_id)

    # OPENVPN
    async def create_ovpn_client(self, client_address: str) -> str:
        return await self.vpn_repo.create_ovpn_client(client_address)

    async def set_ovpn_client(self, client_address: str) -> str:
        return await self.vpn_repo.set_ovpn_client(client_address)

    async def get_ovpn_config(self, client_address: str) -> bytes:
        return await self.vpn_repo.get_ovpn_config(client_address)

    async def delete_client(self, client_address: str):
        await self.vpn_repo.delete_client(client_address)

    async def client_by_address(self, client_address: str) -> list[model.NodeClient]:
        return await self.vpn_repo.client_by_address(client_address)
