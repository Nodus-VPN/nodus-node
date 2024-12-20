from abc import abstractmethod
from typing import Protocol, Any, Sequence
from internal.model.api import wg, vpn
from internal.model import model


class IVPNService(Protocol):

    @abstractmethod
    async def create_wg_client(self, client_address: str) -> str: pass

    @abstractmethod
    async def set_wg_client(self, client_address: str) -> str: pass

    @abstractmethod
    async def get_wg_config(self, wg_client_id: str) -> bytes: pass

    @abstractmethod
    async def create_ovpn_client(self, client_address: str): pass

    @abstractmethod
    async def set_ovpn_client(self, client_address: str): pass

    @abstractmethod
    async def get_ovpn_config(self, client_address: str) -> bytes: pass

    @abstractmethod
    async def delete_client(self, client_address: str): pass

    @abstractmethod
    async def client_by_address(self, client_address: str) -> list[model.NodeClient]: pass


class IVPNRepository(Protocol):
    @abstractmethod
    async def create_wg_client(self, client_address: str) -> str: pass

    @abstractmethod
    async def set_wg_client(self, client_address: str) -> str: pass

    @abstractmethod
    async def get_wg_config(self, wg_client_id: str) -> bytes: pass

    @abstractmethod
    async def create_ovpn_client(self, client_address: str): pass

    @abstractmethod
    async def set_ovpn_client(self, client_address: str): pass

    @abstractmethod
    async def get_ovpn_config(self, client_address: str) -> bytes: pass

    @abstractmethod
    async def delete_client(self, client_address: str): pass

    @abstractmethod
    async def client_by_address(self, client_address: str) -> list[model.NodeClient]: pass


class IMetricsService(Protocol):
    @abstractmethod
    async def health_check(self) -> None: pass


class IContractVPN(Protocol):
    @abstractmethod
    def cost_for_set_node_ip(self, node_ip: str) -> int: pass

    @abstractmethod
    def owner_balance(self) -> int: pass

    @abstractmethod
    def set_node_ip(self, node_ip: str) -> None: pass

    @abstractmethod
    def all_node(self) -> list[str]: pass

    @abstractmethod
    async def get_client(self, client_address: str) -> vpn.VPNClient: pass

    @abstractmethod
    def hashing_client_secret_key(self, client_secret_key: str) -> str: pass


class WGInterface(Protocol):
    @abstractmethod
    async def create_client(self, client_address: str): pass

    @abstractmethod
    async def delete_client(self, wg_client_id: str) -> None: pass

    @abstractmethod
    async def all_client(self) -> list[wg.WGClient]: pass

    @abstractmethod
    async def client_by_address(self, client_address: str) -> wg.WGClient: pass

    @abstractmethod
    async def get_config(self, wg_client_id: str) -> bytes: pass


class OVPNInterface(Protocol):
    @abstractmethod
    def create_client(self, client_address: str): pass

    @abstractmethod
    def delete_client(self, client_address: str) -> None: pass

    @abstractmethod
    def get_config(self, client_address: str) -> bytes: pass


class DBInterface(Protocol):
    @abstractmethod
    async def insert(self, query: str, query_params: dict) -> int: pass

    @abstractmethod
    async def delete(self, query: str, query_params: dict) -> None: pass

    @abstractmethod
    async def update(self, query: str, query_params: dict) -> None: pass

    @abstractmethod
    async def select(self, query: str, query_params: dict) -> Sequence[Any]: pass

    @abstractmethod
    async def multi_query(self, queries: list[str]) -> None: pass
