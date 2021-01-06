#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask import request, jsonify
from app.commons.sqlModel import User
from flask_login import login_required


class UserApi(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        if user is not None:
            return jsonify(user.to_dict())

class Test(Resource):
    def get(self):
        return jsonify({'1':'2'})
