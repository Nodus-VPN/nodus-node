from fastapi import status
from fastapi.responses import JSONResponse

from internal import model
from .schemas import *
from internal.api.http.handlers.status_codes import StatusCodes


def get_wg_config_handler(wg_service: model.IWGService):
    async def get_wg_config(request_data: CreateWGClientRequest):
        try:
            client_data = request_data.model_dump()
            client_address = client_data["client_address"]

            wg_client = await wg_service.client_by_address(client_address)

            if not wg_client:
                wg_client_id = await wg_service.create_client(client_address)
            else:
                wg_client = wg_client[0]
                wg_client_id = wg_client.wg_id

            wg_config = await wg_service.get_config(wg_client_id)
            print(wg_config)
            print(type(wg_config), flush=True)

        except Exception as e:
            raise e

    return get_wg_config
