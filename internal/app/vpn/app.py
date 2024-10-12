from fastapi import FastAPI

from internal.api.http.handlers.vpn.vpn import *

from internal import model


def NewVPN(
        db: model.DBInterface,
        vpn_service: model.IVPNService,
        vpn_contract: model.IContractVPN
):
    app = FastAPI()
    app.add_api_route("/table/create", create_table_handler(db), methods=["GET"], tags=["System"])
    app.add_api_route("/table/drop", drop_table_handler(db), methods=["GET"], tags=["System"])

    include_vpn_handlers(app, vpn_service, vpn_contract)

    return app


def include_vpn_handlers(
        app: FastAPI,
        vpn_service: model.IVPNService,
        vpn_contract: model.IContractVPN
):
    app.add_api_route(
        "/config/wg/{client_address}",
        get_wg_config_handler(vpn_service, vpn_contract),
        methods=["GET"]
    )

    app.add_api_route(
        "/config/ovpn/{client_address}",
        get_ovpn_config_handler(vpn_service, vpn_contract),
        methods=["GET"]
    )

    app.add_api_route(
        "/wg/client/config/{client_address}",
        delete_client_handler(vpn_service),
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
