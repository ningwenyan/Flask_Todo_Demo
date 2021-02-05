#!/usr/bin/env python
# coding=utf-8

"""
  公共API
  可以用以做放权接口
"""


from flask_restful import Resource
from app.commons.sqlModel import User
from flask import jsonify

class ExistEmail(Resource):
    def get(self, raw_email):
        user = User.query.filter_by(email=raw_email).first()
        if user is not None:
            to_dict = {
                'email': raw_email,
                'exist':True
            }
            return jsonify(to_dict)
        else:
            to_dict = {
                'email': raw_email,
                'exist':False
            }
            return jsonify(to_dict)