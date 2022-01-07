import injector
from auctions import AuctionsRepository, GetActiveAuctions, GetSingleAuction
from auctions_infrastructure.queries import SqlGetActiveAuctions, SqlGetSingleAuction
from auctions_infrastructure.repositories import SqlAlchemyAuctionsRepo
from foundation.events import EventBus
from sqlalchemy.engine import Connection

from tasks_infrastructure.models import tasks

__all__ = [
    # module
    "AuctionsInfrastructure",
    # models
    "tasks",

]


class AuctionsInfrastructure(injector.Module):
    @injector.provider
    def get_active_auctions(self, conn: Connection) -> GetActiveAuctions:
        return SqlGetActiveAuctions(conn)

    @injector.provider
    def get_single_auction(self, conn: Connection) -> GetSingleAuction:
        return SqlGetSingleAuction(conn)

    @injector.provider
    def auctions_repo(self, conn: Connection, event_bus: EventBus) -> AuctionsRepository:
        return SqlAlchemyAuctionsRepo(conn, event_bus)
