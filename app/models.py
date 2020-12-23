from app import db


class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String)
    date_active = db.Column(db.DateTime, nullable=False)
    date_inactive = db.Column(db.DateTime)
    purchased_price = db.Column(db.Float)
    sold_price = db.Column(db.Float)
    gain = db.Column(db.Float)


class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String)
    name = db.Column(db.String)
    sector = db.Column(db.String)
    industry = db.Column(db.String)
