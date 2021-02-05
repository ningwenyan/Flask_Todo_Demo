#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from flask_restful import  Api

v3_bp = Blueprint('ap1_v3', __name__, subdomain='api')
v3_api = Api(v3_bp)

from .commons import ExistEmail

v3_api.add_resource(ExistEmail, '/email/<string:raw_email>/', endpoint='email')