from fastapi import FastAPI

from internal.api.http.handlers.wg.wg import *

from internal import model


def NewVPN(
        db: model.DBInterface,
        wg_service: model.IWGService
):
    app = FastAPI()
    app.add_api_route("/table/create", create_table_handler(db), methods=["GET"], tags=["System"])
    app.add_api_route("/table/drop", drop_table_handler(db), methods=["GET"], tags=["System"])

    include_wg_handlers(app, wg_service)

    return app


def include_wg_handlers(
        app: FastAPI,
        wg_service: model.IWGService
):
    app.add_api_route(
        "/wg/client/config/{client_address}",
        get_wg_config_handler(wg_service),
        methods=["GET"],
        tags=["Client"],
    )

    app.add_api_route(
        "/wg/client/config/{client_address}",
        delete_wg_config_handler(wg_service),
        methods=["DELETE"],
        tags=["Client"],
    )


def create_table_handler(db: model.DBInterface):
    async def create_table():
        try:
            await db.multi_query(model.create_queries)
        except Exception as e:
            raise e

    return create_table


def drop_table_handler(db: model.DBInterface):
    async def delete_table():
        try:
            await db.multi_query(model.drop_queries)
        except Exception as e:
            raise e

    return delete_table
