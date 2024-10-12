import time

from fastapi import status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

from internal import model


def get_wg_config_handler(
        vpn_service: model.IVPNService,
        vpn_contract: model.IContractVPN
):
    class RequestModel(BaseModel):
        client_secret_key: str

    async def get_wg_config(client_address: str, request_data: RequestModel):
        try:
            client_secret_key = request_data.model_dump()["client_secret_key"]
            vpn_client = await vpn_contract.get_client(client_address)

            if vpn_contract.hashing_client_secret_key(client_secret_key) != vpn_client.hashed_key:
                return "Wrong client secret key"

            if vpn_client.subscription_expiration_date < int(time.time()):
                return "Subscription expired"

            node_client = await vpn_service.client_by_address(client_address)

            if not node_client:
                wg_client_id = await vpn_service.create_wg_client(client_address)
            elif not node_client[0].wg_id:
                wg_client_id = await vpn_service.set_wg_client(client_address)
            else:
                wg_client = node_client[0]
                wg_client_id = wg_client.wg_id

            wg_config = await vpn_service.get_wg_config(wg_client_id)

            return Response(wg_config, media_type='text/plain')
        except Exception as e:
            raise e

    return get_wg_config


def get_ovpn_config_handler(
        vpn_service: model.IVPNService,
        vpn_contract: model.IContractVPN
):
    class RequestModel(BaseModel):
        client_secret_key: str

    async def get_ovpn_config(client_address: str, request_data: RequestModel):
        try:
            client_secret_key = request_data.model_dump()["client_secret_key"]
            vpn_client = await vpn_contract.get_client(client_address)

            if vpn_contract.hashing_client_secret_key(client_secret_key) != vpn_client.hashed_key:
                return "Wrong client secret key"

            if vpn_client.subscription_expiration_date < int(time.time()):
                return "Subscription expired"

            node_client = await vpn_service.client_by_address(client_address)

            if not node_client:
                await vpn_service.create_wg_client(client_address)
            elif not node_client[0].ovpn_id:
                await vpn_service.set_ovpn_client(client_address)

            ovpn_config = await vpn_service.get_ovpn_config(client_address)

            return Response(ovpn_config, media_type='text/plain')
        except Exception as e:
            raise e

    return get_ovpn_config


def delete_client_handler(vpn_service: model.IVPNService):
    async def delete_client(client_address: str):
        try:
            await vpn_service.delete_client(client_address)

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'status': 'success'}
            )
        except Exception as e:
            raise e

    return delete_client
