#!/usr/bin/env python
# coding=utf-8

from app.commons.exts import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, Regexp, Length, DataRequired

class CMSLoginForm(FlaskForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱."), DataRequired(message="请输入内容."), Length(1, 64, '请输入正确长度的邮箱地址.')])
    password = PasswordField(validators=[Regexp(regex='^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,32}', message="密码应包含字母数字大小写,至少6位."), Length(6, 32, "密码长于6位"), DataRequired("密码应包含字母数字大小写,至少6位.")])
    confirmed = BooleanField(validators=[])


class AddRoleForm(FlaskForm):
    RoleName = StringField(validators=[DataRequired(message="请使用英文表示")])
    RoleDes = StringField(validators=[DataRequired(message="请使用中文表示")])