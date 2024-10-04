import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    db_user = os.environ.get("DB_USERNAME")
    db_pass = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_name = os.environ.get("DB_NAME")

    secret_key = os.environ.get("SECRET_KEY")

    weed_master_url = os.environ.get("WEED_MASTER_URL")
    # HTTP
    HTTP_PORT = os.environ.get("FILESHARING_STORAGE_PORT")



