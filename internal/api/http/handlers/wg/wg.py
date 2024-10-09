import time

from fastapi import status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

from internal import model


def get_wg_config_handler(
        wg_service: model.IWGService,
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

            wg_client = await wg_service.client_by_address(client_address)

            if not wg_client:
                wg_client_id = await wg_service.create_client(client_address)
            else:
                wg_client = wg_client[0]
                wg_client_id = wg_client.wg_id

            wg_config = await wg_service.get_config(wg_client_id)

            return Response(wg_config, media_type='text/plain')
        except Exception as e:
            raise e

    return get_wg_config


def delete_wg_config_handler(wg_service: model.IWGService):
    async def delete_wg_config(client_address: str):
        try:
            await wg_service.delete_client(client_address)

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'status': 'success'}
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'status': 'success'}
            )

    return delete_wg_config
