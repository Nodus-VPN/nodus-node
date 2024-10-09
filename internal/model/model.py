from dataclasses import dataclass
from datetime import datetime


@dataclass
class NodeClient:
    id: int
    wg_id: str
    ovpn_id: str
    address: str
    traffic: int
    latest_handshake: datetime
    created_at: datetime
    updated_at: datetime

    @classmethod
    def serialize(cls, rows):
        return [cls(
            id=row.id,
            wg_id=row.wg_id,
            ovpn_id=row.ovpn_id,
            address=row.address,
            traffic=row.traffic,
            latest_handshake=row.latest_handshake,
            created_at=row.created_at,
            updated_at=row.updated_at
        ) for row in rows]
