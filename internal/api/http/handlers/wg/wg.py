from fastapi import status
from fastapi.responses import JSONResponse, FileResponse

from internal import model
from .schemas import *
from internal.api.http.handlers.status_codes import StatusCodes


def get_wg_config_handler(wg_service: model.IWGService):
    async def get_wg_config(client_address: str):
        try:
            wg_client = await wg_service.client_by_address(client_address)

            if not wg_client:
                wg_client_id = await wg_service.create_client(client_address)
            else:
                wg_client = wg_client[0]
                wg_client_id = wg_client.wg_id

            wg_config = await wg_service.get_config(wg_client_id)

            return FileResponse(wg_config, media_type='text/plain', filename=f"wg.conf")
        except Exception as e:
            raise e

    return get_wg_config
