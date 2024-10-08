from internal import model


class MetricsService(model.IMetricsService):
    def __init__(
            self,
            db: model.DBInterface,
            wg: model.WGInterface,
    ):
        self.db = db
        self.wg = wg

    async def health_check(self) -> None:
        await self.wg.all_client()
        await self.db.select("SELECT * FROM clients WHERE id = :id", {"id": 1})

    async def traffic(self) -> int:
        traffic_acc = 0
        all_client = await self.wg.all_client()

        for client in all_client:
            traffic_acc += client.transferRx + client.transferTx
        return traffic_acc
