from fastapi import status
from fastapi.responses import JSONResponse

from internal import model
from .schemas import *
from internal.api.http.handlers.status_codes import StatusCodes


def create_wg_client_handler(wg_service: model.IWGService):
    async def create_tokens(request_data: CreateWGClientRequest):
        try:
            client_data = request_data.model_dump()
            client_address = client_data["client_address"]

            wg_client = await wg_service.client_by_address(client_address)

            if not wg_client:
                return JSONResponse(
                    status_code=status.HTTP_409_CONFLICT,
                    content={
                        "error": "Client already exists",
                        "status": StatusCodes.CLIENT_EXIST.value
                    }
                )

            wg_client_id = await wg_service.create_client(client_address)

        except Exception as e:
            raise e

    return create_tokens
