from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flaskext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object('settings')

Bootstrap(app)
Markdown(app, extension=['fenced_code', 'tables'])
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

# migrate
migrate = Migrate(app, db)

from blog import views
from author import views