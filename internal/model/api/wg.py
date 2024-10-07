from dataclasses import dataclass


@dataclass
class WGClient:
    id: str
    name: str
    enabled: bool
    address: str
    publicKey: str
    createdAt: str
    updatedAt: str
    downloadableConfig: bool
    persistentKeepalive: str
    latestHandshakeAt: str
    transferRx: int
    transferTx: int
