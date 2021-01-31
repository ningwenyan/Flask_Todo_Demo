#!/usr/bin/env python
# coding=utf-8
from flask import Blueprint

cms_bp = Blueprint('cms', __name__, subdomain='cms')


from . import views