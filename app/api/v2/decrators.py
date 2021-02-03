#!/usr/bin/env python
# coding=utf-8

from functools import wraps
from flask_login import current_user
from flask import jsonify


def admin_login(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_superadmin():
            return func(*args, **kwargs)
        else:
            to_dict = {
                'info': '你没有权限'
            }
            return jsonify(to_dict)
    return wrappers
