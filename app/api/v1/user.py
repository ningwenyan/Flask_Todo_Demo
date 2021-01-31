#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource, fields, marshal_with
from flask import request, jsonify
from app.commons.sqlModel import User
from flask_login import login_required


class UserApi(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        if user is not None:
            return jsonify(user.to_dict())


class User_update_username(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        if user is not None:
            return jsonify(user.to_dict())

    def post(self, id):
        user = User.query.get_or_404(id)
        print(request.json.get('url'))
        print(user.have_permission(request.json.get('url')))

        if user is not None and user.have_permission(request.json.get('url')) and request.json.get('username'):
            user.username = request.json.get('username')
            user.save()
            return jsonify(user.to_dict())
        else:
            to_dict = {
                'flag': False
            }
            return jsonify(to_dict)


class Test(Resource):
    def get(self):
        return jsonify({'1':'2'})
