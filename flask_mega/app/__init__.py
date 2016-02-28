import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir
from momentjs import momentjs
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Translation.
babel = Babel(app)

# Login Related
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# Mail
mail = Mail(app)

# Include Custom class into Jinja engine.
app.jinja_env.globals['momentjs'] = momentjs

from app import views, models