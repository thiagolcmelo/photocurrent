from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('settings')
Bootstrap(app)
Markdown(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# migrate
migrate = Migrate(app, db)

from blog import views
from author import views