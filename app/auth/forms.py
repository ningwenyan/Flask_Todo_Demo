#!/usr/bin/env python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo
from app.commons.sqlModel import User

class AuthLoginForm(FlaskForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱."), DataRequired(message="请输入内容."), Length(1, 64, '请输入正确长度的邮箱地址.')])
    password = PasswordField(validators=[Regexp(regex='^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,32}', message="密码应包含字母数字大小写,至少6位."), Length(6, 32, "密码长于6位"), DataRequired("密码应包含字母数字大小写,至少6位.")])
    code = StringField(validators=[Regexp(regex='^[A-Za-z0-9]+$', message="验证码只包含字母数字大小写"), Length(4, 4 , '请输入正确的验证码.'), DataRequired("请输入4位验证码")])
    confirmed = BooleanField(validators=[])


class AuthRegisterForm(FlaskForm):
    username = StringField(validators=[Length(1, 24, "请输入24位字符之内")])
    email = StringField(validators=[Email(message="请输入正确的邮箱."), DataRequired(message="请输入内容."), Length(1, 64, '请输入正确长度的邮箱地址.')])
    password = PasswordField(validators=[Regexp(regex='^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,32}', message="密码应包含字母数字大小写,至少6位."), Length(6, 32, "密码长于6位"), DataRequired("密码应包含字母数字大小写,至少6位.")])
    password2 = PasswordField(validators=[EqualTo('password', message="密码不一致")])
    code = StringField(validators=[Regexp(regex='^[A-Za-z0-9]+$', message="验证码只包含字母数字大小写"), Length(4, 4 , '请输入正确的验证码.'), DataRequired("请输入4位验证码")])
    confirmed = BooleanField(validators=[])

    # 自定义Field,验证邮箱和用户
    def validate_email(self, field):
        """将邮箱地址全部转换为小写"""
        if User.query.filter_by(email = field.data.lower()).first():
            raise ValidationError("邮箱已注册")

    def validata_username(self, field):
        """注意: _username 是类的私有属性,要在sqlModel中添加映射"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("用户名已存在")