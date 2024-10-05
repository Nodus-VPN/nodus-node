import time

from internal import model


def NewClientChecker(
        contract: model.IContractVPN,
        client_service: model.IClientService,
        price_per_day: int
):
    while True:
        clients_address = client_service.all_client_address()

        for client_address in clients_address:
            client_balance = contract.client_balance(client_address)

            if client_balance > price_per_day:
                client_service.delete_client(client_address)
        time.sleep(60*60*12)
