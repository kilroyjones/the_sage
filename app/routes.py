import json
from flask import (
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    jsonify,
)
from app.models import Holding
from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/holdings")
def holdings():
    holdings = Holding.query.filter_by(date_inactive=None)
    return jsonify([holding.as_dict() for holding in holdings])
