from app import scheduler, finnhub_client
from app.models import Holding


@scheduler.task("interval", id="update_holdings", seconds=5, misfire_grace_time=900)
def update_holdings():
    res = finnhub_client.quote("AAPL")
    print(res)


@scheduler.task("interval", id="create_holding", seconds=15, misfire_grace_time=900)
def create_holding():
    pass
