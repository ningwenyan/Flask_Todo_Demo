#!/usr/bin/env python
# coding=utf-8

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_uploads import UploadSet

bootstrap = Bootstrap()
login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()
mail = Mail()
photos = UploadSet('PHOTO')