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

contract_abi = """[{
    "inputs": [
        {
            "internalType": "address",
            "name": "_nds_address",
            "type": "address"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
},
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "node_id",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "node_ip",
                "type": "string"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "node_owner",
                "type": "address"
            }
        ],
        "name": "SetNode",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_ip",
                "type": "string"
            }
        ],
        "name": "setNodeIP",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "availableNodes",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAllNode",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_client",
                "type": "address"
            }
        ],
        "name": "getClientBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "NDS",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "nodeOwners",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]"""
contract_vpn = ContractVPN(
    owner_address="0xBb35CB00d1e54A98b6a44E4F42faBedD43660293",
    owner_private_key="2dca2cd0db77495ca32f08e601457bb75fc0b8d92d6f4e654792334554d80f85",
    contract_abi=contract_abi,
    contract_address="0xF7190873c75Aafd295B1a466c24a2e144adeCBA9"
)


db = PG(cfg.db_user, cfg.db_pass, cfg.db_host, cfg.db_port, cfg.db_name)

wg = WG(cfg.wg_host)
wg_repository = WGRepository(db, wg)
wg_service = WGService(wg_repository)

if __name__ == '__main__':
    args = parser.parse_args()

    if args.app == "http":
        app = NewHttp(db, wg_service)

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
