from web3 import AsyncWeb3, Web3


class Contract:
    sender_private_key = "2dca2cd0db77495ca32f08e601457bb75fc0b8d92d6f4e654792334554d80f85"
    sender_address = "0xBb35CB00d1e54A98b6a44E4F42faBedD43660293"

    def __init__(self, contract_address: str, contract_abi: list):
        w3 = Web3(Web3.HTTPProvider('https://rpc.cardona.zkevm-rpc.com'))
        checksum_address = Web3.to_checksum_address(contract_address)

        self.contract = w3.eth.contract(checksum_address, abi=contract_abi)
        self.checksum_address = Web3.to_checksum_address(contract_address)
        self.w3 = w3

    def _send_transaction(self, function):
        gas_estimate = function.estimate_gas({'from': self.sender_address})
        gas_price = self.w3.eth.gas_price
        transaction = function.build_transaction({
            'from': self.sender_address,
            'gas': gas_estimate,
            'gasPrice': gas_price,
            'nonce': self.w3.eth.get_transaction_count(Web3.to_checksum_address(self.sender_address))
        })
        signed_tx = self.w3.eth.account.sign_transaction(transaction, self.sender_private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt

    def get_balance(self) -> int:
        return self.w3.eth.get_balance(self.checksum_address)

    def set_node_ip(self):
        function = self.contract.functions.setNodeIP("12412214")
        tx_receipt = self._send_transaction(function)
        return tx_receipt


abi = [
    {
        "inputs": [],
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
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "node_id",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "node_ip",
                "type": "string"
            },
            {
                "indexed": False,
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
    }
]
contract = Contract(
    contract_address="0x4a010B1b9E5f75cfF8ba515a5D5cd955756cC06D",
    contract_abi=abi
)
print(contract.set_node_ip())
