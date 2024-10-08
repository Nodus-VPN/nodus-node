from fastapi import FastAPI

from internal.api.http.handlers.metrics.metrics import *

from internal import model

PREFIX = "/api"


def NewMetrics(
        db: model.DBInterface,
        metrics_service: model.IMetricsService,
):
    app = FastAPI(root_path=PREFIX)
    app.add_api_route("/table/create", create_table_handler(db), methods=["GET"], tags=["System"])
    app.add_api_route("/table/drop", drop_table_handler(db), methods=["GET"], tags=["System"])

    include_metrics_handlers(app, metrics_service)

    return app


def include_metrics_handlers(
        app: FastAPI,
        metrics_service: model.IMetricsService,
):
    app.add_api_route(
        "/health",
        health_check_handler(metrics_service),
        methods=["GET"],
        tags=["Metrics"],
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
