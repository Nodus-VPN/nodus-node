import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    db_user = "postgres"
    db_pass = "postgres"
    db_host = "postgres_db"
    db_port = 5432
    db_name = "postgres"

    wg_host = "wg_easy"
    owner_address = os.getenv("OWNER_ADDRESS")
    owner_private_key = os.getenv("OWNER_PRIVATE_KEY")

    node_ip: str = os.getenv("NODE_IP")
    HTTP_PORT: int = 7000
    price_per_day: int = 100
