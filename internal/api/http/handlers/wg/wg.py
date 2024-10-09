from fastapi import status
from fastapi.responses import JSONResponse, Response

from internal import model


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
            raise e

    return delete_wg_config
