import uvicorn

from infrastructure.pg.pg import PG
from internal.app.http.app import NewHttp

from pkg.api import WGClient
from internal.config import config

import argparse

parser = argparse.ArgumentParser(description='For choice app')
parser.add_argument(
    'app',
    type=str,
    help='Option: "http, init"'
)

secret_key = config.get("SECRET_KEY")

db_user = config.get("DB_USER")
db_pass = config.get("DB_PASS")
db_host = config.get("DB_HOST")
db_port = config.get("DB_PORT")
db_name = config.get("DB_NAME")

auth_host = config.get("FILESHARING_AUTH_HOST")
auth_port = config.get("FILESHARING_AUTH_PORT")


# INFRASTRUCTURE
db = PG(db_user, db_pass, db_host, db_port, db_name)

# INTERCONNECTION
crypto_client = CryptoClient()
auth_client = AuthClient(auth_host, auth_port)

# DEPENDENCIES
subscription_repo = SubscriptionRepo(db)
subscription_service = SubscriptionService(subscription_repo, crypto_client)

if __name__ == '__main__':
    args = parser.parse_args()
    http_port = config.get("FILESHARING_SUBSCRIPTION_PORT")

    if args.app == "http":
        app = NewHttp(
            db,
            subscription_service,
            auth_client,
            secret_key
        )
        uvicorn.run(app, host="0.0.0.0", port=int(http_port))
