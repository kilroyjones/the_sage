import datetime
import time
from app import scheduler, finnhub_client, db
from app.models import Holding, Ticker
from sqlalchemy.sql.expression import func, select


# @scheduler.task("interval", id="update_holdings", seconds=3, misfire_grace_time=900)
# @scheduler.task("interval", id="update_holdings", minutes=30, misfire_grace_time=900)
def update_holdings():
    holdings = Holding.query.filter_by(date_inactive=None)
    count = 0
    for holding in holdings:
        quote = finnhub_client.quote(holding.ticker)
        holding.current_price = quote["c"]
        db.session.commit()
        count += 1
        if count % 10 == 0:
            time.sleep(1)


@scheduler.task("interval", id="create_holding", seconds=3, misfire_grace_time=900)
# @scheduler.task("interval", id="create_holding", hours=72, misfire_grace_time=900)
def create_holding():
    stock = Ticker.query.order_by(func.random()).first()
    quote = finnhub_client.quote(stock.ticker)
    holding = Holding(
        ticker=stock.ticker,
        name=stock.name,
        date_active=datetime.datetime.now(),
        date_inactive=None,
        purchased_price=quote["c"],
        current_price=quote["c"],
        sold_price=-1,
        gain=0.0,
    )
    db.session.add(holding)
    db.session.commit()
