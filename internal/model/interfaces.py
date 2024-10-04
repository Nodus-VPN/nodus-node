from abc import abstractmethod
from typing import Protocol, Any, Sequence


class IContractVPN(Protocol):
    @abstractmethod
    def client_balance(self, client_address: str) -> int: pass

    @abstractmethod
    def cost_for_set_node_ip(self, node_ip: str) -> int: pass

    @abstractmethod
    def sender_balance(self) -> int: pass

    @abstractmethod
    def set_node_ip(self, node_ip: str) -> None: pass


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
