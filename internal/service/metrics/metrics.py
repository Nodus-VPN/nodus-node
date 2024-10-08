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