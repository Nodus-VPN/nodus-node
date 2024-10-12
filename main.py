import uvicorn

from infrastructure.pg.pg import PG
from infrastructure.wg.wg import WG
from infrastructure.ovpn.ovpn import OVPN

from pkg.contracts.vpn import ContractVPN

from internal.app.init_node.app import InitNode
from internal.app.vpn.app import NewVPN
from internal.app.metrics.app import NewMetrics

from internal.service.wg.wg import WGService
from internal.repository.wg.wg import WGRepository

from internal.service.metrics.metrics import MetricsService

from internal.config.config import Config as cfg
import argparse

parser = argparse.ArgumentParser(description='For choice app')
parser.add_argument(
    'app',
    type=str,
    help='Option: "vpn, init_node, metrics"'
)

vpn_contract = ContractVPN(
    owner_address=cfg.owner_address,
    owner_private_key=cfg.owner_private_key,
    contract_abi=cfg.vpn_contract_abi,
    contract_address=cfg.vpn_contract_address,
    hash_key=cfg.hash_key
)


db = PG(cfg.db_user, cfg.db_pass, cfg.db_host, cfg.db_port, cfg.db_name)

wg = WG(cfg.wg_host, cfg.wg_port)
wg_repository = WGRepository(db, wg)
wg_service = WGService(wg_repository)

metrics_service = MetricsService(db, wg)

if __name__ == '__main__':
    args = parser.parse_args()

    if args.app == "init_node":
        InitNode(
            vpn_contract,
            cfg.node_ip
        )

    if args.app == "vpn":
        app = NewVPN(db, wg_service, vpn_contract)
        uvicorn.run(app, host="0.0.0.0", port=cfg.vpn_port)

    if args.app == "metrics":
        app = NewMetrics(db, metrics_service)
        uvicorn.run(app, host="0.0.0.0", port=cfg.metrics_port)

    if args.app == "test":
        ovpn = OVPN()
        ovpn.create_client("admin")
        config = ovpn.get_config("admin")
        ovpn.delete_client("admin")
        print(config.decode("utf-8"))


