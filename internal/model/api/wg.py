from dataclasses import dataclass


@dataclass
class WGClient:
    id: str
    name: str
    enable: bool
    address: str
    public_key: str
    createdAt: str
    updatedAt: str
    downloadableConfig: bool
    persistentKeepalive: str
    latestHandshakeAt: str
    transferRx: int
    transferTx: int
