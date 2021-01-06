#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from flask_restful import  Api

v1_bp = Blueprint('ap1_v1', __name__, url_prefix='/api/v1')
v1_api = Api(v1_bp)


from .user import UserApi, Test

v1_api.add_resource(UserApi, '/userApi/<int:id>/')
v1_api.add_resource(Test, '/test/')