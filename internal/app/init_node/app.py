from internal import model


def InitNode(
        contract: model.IContractVPN,
        node_ip: str
):
    transaction_cost = contract.cost_for_set_node_ip("node_ip")
    sender_balance = contract.sender_balance()

    if transaction_cost >= sender_balance:
        print("Недостаточно средств")

    contract.set_node_ip(node_ip)
