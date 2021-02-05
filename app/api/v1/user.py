#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask import request, jsonify
from app.commons.sqlModel import User
from app.utils.sendMail import sendMail


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
        if user is not None and user.have_permission(request.json.get('url')) and request.json.get('username'):
            user.username = request.json.get('username')
            user.save()
            return jsonify(user.to_dict())
        else:
            to_dict = {
                'flag': False
            }
            return jsonify(to_dict)


class User_update_email(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        if user is not None:
            return jsonify(user.to_dict())

    def post(self, id):
        user = User.query.get_or_404(id)
        if user is not None and request.json.get('email') and user.have_permission(request.json.get('url')):
            # 生成邮箱token
            token = user.generate_change_email_token(request.json.get('email'))
            # 发送邮件
            sendMail(user.email, '修改邮箱地址', 'changeEmail', user=user, token=token)
            to_dict = {
                'success': '发送邮件成功'
            }
            return jsonify(to_dict)
        else:
            to_dict = {
                'error': '你没有权限'
            }
            return jsonify(to_dict)




class Test(Resource):
    def get(self):
        return jsonify({'1':'2'})
