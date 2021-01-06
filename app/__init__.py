import os
import finnhub
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SCHEDULER_API_ENABLED"] = True
finnhub_client = finnhub.Client(api_key=app.config["FINN_KEY"])

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)  # this
CORS(app)

# scheduler = APScheduler()
# scheduler.init_app(app)
# scheduler.start()

from app import routes
from app.models import Ticker, Holding

# from app.cronjobs import *
