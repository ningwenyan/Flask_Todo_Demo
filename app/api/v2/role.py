#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask import request, jsonify
from app.commons.sqlModel import Role, User
from .decrators import admin_login


class GetAllRoles(Resource):
   # method_decorators = [admin_login]
    def get(self):
        roles = Role.query.all()
        real_roles = []
        for role in roles:
            real_roles.append(role.description)
        to_dict = {'roles': real_roles}
        return jsonify(to_dict)

    def post(self):
        if request.json.get('name') and request.json.get('description'):
            role = Role(request.json.get('name'), request.json.get('description'))
            role.save()
        roles = Role.query.all()
        real_roles = []
        for role in roles:
            real_roles.append(role.description)
        to_dict = {'roles': real_roles}
        return jsonify(to_dict)



class UpdateUserRole(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        if user is not None:
            roles = [role.description for role in user.roles]
            to_dict = {
                'user_id': user.id,
                'roles' : roles
            }
            return jsonify(to_dict)


    def post(self, id):
        user = User.query.get_or_404(id)
        if request.json.get('roles') and user is not None:
            real_roles = [ role.strip() for role in request.json.get('roles')]
            user_role = []
            for role in real_roles:
                if Role.query.filter_by(description=role).first() is not None:
                    real_role = Role.query.filter_by(description=role).first()
                    user_role.append(real_role)
            user.roles = user_role
            user.save()
            roles = [role.description for role in user.roles]
            to_dict = {
                'user_id': user.id,
                'roles': roles
            }
            return jsonify(to_dict)