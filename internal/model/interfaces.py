from abc import abstractmethod
from typing import Protocol, Any, Sequence
from internal.model.api.wg import WGClient


class IWGService(Protocol):

    @abstractmethod
    async def create_client(self, client_address: str): pass

    @abstractmethod
    async def delete_client(self, client_address: str): pass

    @abstractmethod
    async def client_by_address(self, client_address: str): pass


class IWGRepository(Protocol):
    @abstractmethod
    async def create_client(self, client_address: str) -> str: pass

    @abstractmethod
    async def delete_client(self, client_address: str): pass

    @abstractmethod
    async def client_by_address(self, client_address: str): pass


class IClientService(Protocol):
    @abstractmethod
    def all_client_address(self) -> list: pass

    @abstractmethod
    def delete_client(self, client_address: str) -> None: pass


class IClientRepository(Protocol):
    @abstractmethod
    def all_client_address(self) -> list: pass


class IContractVPN(Protocol):
    @abstractmethod
    def client_balance(self, client_address: str) -> int: pass

    @abstractmethod
    def cost_for_set_node_ip(self, node_ip: str) -> int: pass

    @abstractmethod
    def owner_balance(self) -> int: pass

    @abstractmethod
    def set_node_ip(self, node_ip: str) -> None: pass

    @abstractmethod
    def all_node(self) -> list[str]: pass


class WGInterface(Protocol):
    @abstractmethod
    async def create_client(self, client_address: str): pass

    @abstractmethod
    async def delete_client(self, client_address: str) -> None: pass

    @abstractmethod
    async def all_client(self) -> list[WGClient]: pass

    @abstractmethod
    async def client_by_address(self, client_address: str) -> WGClient: pass


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
