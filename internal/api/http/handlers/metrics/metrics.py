from fastapi import status
from fastapi.responses import JSONResponse

from internal import model


def health_check_handler(
        metrics_service: model.IMetricsService,
):
    async def health_check():
        try:
            await metrics_service.health_check()

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"health": True}
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"health": False},
            )

    return health_check


def get_traffic_handler(
        metrics_service: model.IMetricsService,
):
    async def get_traffic():
        try:
            traffic = await metrics_service.traffic()

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"traffic": traffic}
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"health": False},
            )

    return get_traffic
