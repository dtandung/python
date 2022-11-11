from flask import Flask
from config import Config
app = Flask(__name__)

from app import routes
#app.config["SECRET_KEY"] = "hard-secret-key"
app.config.from_object(Config)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.app_context().push()
from app import models