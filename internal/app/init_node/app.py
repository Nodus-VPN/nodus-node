from internal import model


def InitNode(
        contract: model.IContractVPN,
        node_ip: str
) -> str:
    transaction_cost = contract.cost_for_set_node_ip("node_ip")
    sender_balance = contract.owner_balance()

    if transaction_cost >= sender_balance:
        return "Недостаточно средств"

    contract.set_node_ip(node_ip)
    return f"Инициализация прошла успешно, ваш IP: {node_ip}"
