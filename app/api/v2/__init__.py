#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from flask_restful import  Api
from .decrators import admin_login

v2_bp = Blueprint('ap1_v2', __name__, url_prefix='/api/v2', subdomain='cms')
v2_api = Api(v2_bp, decorators=[admin_login])


from .role import GetAllRoles, UpdateUserRole

v2_api.add_resource(GetAllRoles, '/roleApi/', endpoint="roleApi")
v2_api.add_resource(UpdateUserRole, '/UpdateUserRole/<int:id>/', endpoint='UpdateUserRole')

from .resource import GetAllResource, UpdateRoleResource, GetURLMap

v2_api.add_resource(GetAllResource, '/resourceApi/', endpoint='resourceApi')
v2_api.add_resource(UpdateRoleResource, '/UpdateRoleResource/<int:id>/', endpoint='UpdateRoleResource')
v2_api.add_resource(GetURLMap, '/GetURLMap/', endpoint='GetURLMap')