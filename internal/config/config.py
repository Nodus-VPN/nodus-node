import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    db_user = "postgres"
    db_pass = "postgres"
    db_host = "nodus-db"
    db_port = 5432
    db_name = "postgres"

    wg_host = "wg-easy"
    wg_port = 51821

    owner_address = os.getenv("OWNER_ADDRESS")
    owner_private_key = os.getenv("OWNER_PRIVATE_KEY")

    node_ip: str = os.getenv("NODE_IP")
    vpn_port: int = 7000
    metrics_port: int = 7001
    hash_key: str = "city"

    vpn_contract_address: str = "0x66c8352889121247EB4F10C27e720B342A4F1C8a"
    vpn_contract_abi: str = """[
        {
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
            "name": "allClientAddress",
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
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "allNodeIp",
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
            "inputs": [
                {
                    "internalType": "string",
                    "name": "nodeIP",
                    "type": "string"
                }
            ],
            "name": "calculateNodeScore",
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
            "name": "calculateReward",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "clients",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "hashedKey",
                    "type": "string"
                },
                {
                    "internalType": "uint256",
                    "name": "subscriptionExpirationDate",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string[]",
                    "name": "_nodeIP",
                    "type": "string[]"
                }
            ],
            "name": "deleteNode",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getAllClientAddress",
            "outputs": [
                {
                    "internalType": "address[]",
                    "name": "",
                    "type": "address[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getAllNodeIp",
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
                    "name": "_clientAddress",
                    "type": "address"
                }
            ],
            "name": "getClient",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "string",
                            "name": "hashedKey",
                            "type": "string"
                        },
                        {
                            "internalType": "uint256",
                            "name": "subscriptionExpirationDate",
                            "type": "uint256"
                        }
                    ],
                    "internalType": "struct VPN.Client",
                    "name": "",
                    "type": "tuple"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
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
            "inputs": [
                {
                    "internalType": "string",
                    "name": "_nodeIP",
                    "type": "string"
                }
            ],
            "name": "getNode",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "id",
                            "type": "uint256"
                        },
                        {
                            "internalType": "string",
                            "name": "status",
                            "type": "string"
                        },
                        {
                            "internalType": "address",
                            "name": "owner",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "okResponse",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "failedResponse",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "downloadSpeedRN",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "uploadSpeedRN",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "packageLossRN",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256",
                            "name": "pingRN",
                            "type": "uint256"
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "downloadSpeedTS",
                            "type": "uint256[]"
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "uploadSpeedTS",
                            "type": "uint256[]"
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "packageLossTS",
                            "type": "uint256[]"
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "pingTS",
                            "type": "uint256[]"
                        },
                        {
                            "internalType": "uint256",
                            "name": "reward",
                            "type": "uint256"
                        }
                    ],
                    "internalType": "struct VPN.Node",
                    "name": "",
                    "type": "tuple"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "name": "nodes",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "id",
                    "type": "uint256"
                },
                {
                    "internalType": "string",
                    "name": "status",
                    "type": "string"
                },
                {
                    "internalType": "address",
                    "name": "owner",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "okResponse",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "failedResponse",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "downloadSpeedRN",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "uploadSpeedRN",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "packageLossRN",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "pingRN",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "reward",
                    "type": "uint256"
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
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "_nodeIP",
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
                    "internalType": "uint256",
                    "name": "_subscriptionDuration",
                    "type": "uint256"
                },
                {
                    "internalType": "string",
                    "name": "_hashedKey",
                    "type": "string"
                }
            ],
            "name": "subscribe",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "subscriptionMounthPrice",
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
            "inputs": [
                {
                    "internalType": "string[]",
                    "name": "_nodeIP",
                    "type": "string[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_downloadSpeed",
                    "type": "uint256[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_uploadSpeed",
                    "type": "uint256[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_packageLoss",
                    "type": "uint256[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_ping",
                    "type": "uint256[]"
                }
            ],
            "name": "updateNodeMetrics",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string[]",
                    "name": "_nodeIP",
                    "type": "string[]"
                },
                {
                    "internalType": "string",
                    "name": "_status",
                    "type": "string"
                }
            ],
            "name": "updateNodeStatus",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string[]",
                    "name": "_nodeIP",
                    "type": "string[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_okResponse",
                    "type": "uint256[]"
                },
                {
                    "internalType": "uint256[]",
                    "name": "_failedResponse",
                    "type": "uint256[]"
                }
            ],
            "name": "updateNodeUptime",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]"""