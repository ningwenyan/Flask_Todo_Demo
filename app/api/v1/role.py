#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask import request, jsonify
from app.commons.sqlModel import Role


class GetAllRoles(Resource):

    def get(self):
        roles = Role.query.all()
        real_roles = []
        for role in roles:
            real_roles.append(role.name)

        to_dict = {'roles': real_roles}
        return jsonify(to_dict)