#!/usr/bin/env python
# coding=utf-8

from . import auth_bp
from flask import render_template, redirect, url_for, flash, request
from .forms import AuthLoginForm
from app.commons.exts import db
from app.commons.sqlModel import User
from flask_login import login_user
from datetime import timedelta

# 登录
@auth_bp.route('/login/', methods=['GET', 'POST'])
def auth_login():
    form = AuthLoginForm()
    if form.validate_on_submit():
        # 验证邮箱和密码
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            """
            :判断confirm,确定是否要自动登录
            :使用 user.seen() 自动更新登录时间
            """
            if form.confirmed.data:
                login_user(user.seen(), remember=True, duration=timedelta(days=30))
            else:
                login_user(user.seen())
            # 判断next
            url_next = request.args.get("next")
            if url_next is None or not url_next.startswith('/'):
                url_next = url_for('main.index')
            return redirect(url_for('main.index') or url_next)
        else:
            flash("无效的用户名和密码")
    return render_template('auth/login.html', form=form)


# 注册
@auth_bp.route('/register/')
def auth_register():
    return render_template('auth/register.html')