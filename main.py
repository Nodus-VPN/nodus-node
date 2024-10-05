from infrastructure.pg.pg import PG
from infrastructure.wg.wg import WG

from pkg.contracts.vpn import ContractVPN

from internal.app.init_node.app import InitNode
from internal.app.client_checker.app import NewClientChecker
from internal.app.http.app import NewHttp

from internal.service.wg.wg import WGService
from internal.repository.wg.wg import WGRepository

from internal.config.config import Config as cfg
import argparse

parser = argparse.ArgumentParser(description='For choice app')
parser.add_argument(
    'app',
    type=str,
    help='Option: "http, init_node, client_checker"'
)

contract_vpn = ContractVPN(
    owner_address=cfg.owner_address,
    owner_private_key=cfg.owner_private_key,
    contract_abi=cfg.contract_abi,
    contract_address=cfg.contract_address
)


# db = PG(cfg.db_user, cfg.db_pass, cfg.db_host, cfg.db_port, cfg.db_name)
#
# wg = WG(cfg.wg_host)
# wg_repository = WGRepository(db, wg)
# wg_service = WGService(wg_repository)

if __name__ == '__main__':
    args = parser.parse_args()

    # if args.app == "http":
    #     app = NewHttp(db, wg_service)

    if args.app == "init_node":
        result = InitNode(
            contract_vpn,
            cfg.node_ip
        )
        print(result)

    # if args.app == "client_checker":
    #     NewClientChecker(
    #
    #     )
