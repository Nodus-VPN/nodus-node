from dataclasses import dataclass
import requests


@dataclass
class Config:
    db_user = "postgres"
    db_pass = "postgres"
    db_host = "postgres_db"
    db_port = 5432
    db_name = "postgres"

    wg_host = "wg_easy"
    owner_address = input("Введите ваш адрес кошелька ERC20:")
    owner_private_key = input(f"Введите private_key от вашего кошелька {owner_address}:")

    node_ip: str = requests.get("http://icanhazip.com").text
    HTTP_PORT: int = 7000
    price_per_day: int = 100



