from dataclasses import dataclass


@dataclass
class VPNClient:
    hashed_key: str
    subscription_expiration_date: int
