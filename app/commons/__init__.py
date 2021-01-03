#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

commons_bp = Blueprint('commons', __name__, url_prefix='/commons')

from . import exts
from . import sqlModel
from . import errors
from . import views