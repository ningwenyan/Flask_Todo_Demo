#!/usr/bin/env python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, Length, Regexp


class AuthLoginForm(FlaskForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱."), DataRequired(message="请输入内容."), Length(1, 64, '请输入正确长度的邮箱地址.')])
    password = PasswordField(validators=[Regexp(regex='^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,32}', message="密码应包含字母数字大小写,至少6位."), Length(6, 32, "密码长于6位"), DataRequired("密码应包含字母数字大小写,至少6位.")])
    code = StringField(validators=[Regexp(regex='^[A-Za-z0-9]+$', message="验证码只包含字母数字大小写"), Length(4, 4 , '请输入正确的验证码.'), DataRequired("请输入4位验证码")])
    confirmed = BooleanField(validators=[])