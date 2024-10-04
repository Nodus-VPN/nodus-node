import requests

from pkg.contracts.vpn import ContractVPN
from internal.app.init_node.app import InitNode

import argparse
parser = argparse.ArgumentParser(description='For choice app')
parser.add_argument(
    'app',
    type=str,
    help='Option: "http, init_node"'
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
    sender_address="0xBb35CB00d1e54A98b6a44E4F42faBedD43660293",
    sender_private_key="2dca2cd0db77495ca32f08e601457bb75fc0b8d92d6f4e654792334554d80f85",
    contract_abi=contract_abi,
    contract_address="0xF7190873c75Aafd295B1a466c24a2e144adeCBA9"
)

node_ip = requests.get("http://icanhazip.com").text

if __name__ == '__main__':
    args = parser.parse_args()

    if args.app == "init_node":
        InitNode(
            contract_vpn,
            node_ip
        )
