import sys

from internal import model


def InitNode(
        contract: model.IContractVPN,
        node_ip: str
):
    all_node = contract.all_node()
    if node_ip in all_node:
        print(f"Вы уже инициализировались ранее, ваш IP: {node_ip}")
        sys.exit(0)

    transaction_cost = contract.cost_for_set_node_ip(node_ip)
    sender_balance = contract.owner_balance()

    if transaction_cost >= sender_balance:
        print("Недостаточно средств")
        sys.exit(1)

    contract.set_node_ip(node_ip)
    print(f"Инициализация прошла успешно, ваш IP: {node_ip}")
    sys.exit(0)
