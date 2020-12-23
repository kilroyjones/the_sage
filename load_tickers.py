from app.models import Ticker
from app import db
import csv


def get_tickers(path):
    tickers = []
    with open(path) as csvfile:
        stocks = csv.reader(csvfile, delimiter=",")
        for stock in stocks:
            ticker, name, _, _, _, sector, industry, _, _ = stock
            tickers.append([ticker, name, sector, industry])
    return tickers


def add_to_db(tickers):
    for ticker in tickers:
        ticker, name, sector, industry = ticker
        if db.session.query(Ticker.ticker).filter_by(ticker=ticker).scalar() is None:
            ticker = Ticker(ticker=ticker, name=name, sector=sector, industry=industry)
            db.session.add(ticker)
            db.session.commit()


if __name__ == "__main__":
    tickers = get_tickers("data/nasdaq.csv") + get_tickers("data/nyse.csv")
    add_to_db(tickers)
