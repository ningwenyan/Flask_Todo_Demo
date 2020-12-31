#!/usr/bin/env python
# coding=utf-8

from . import auth_bp
from flask import render_template, redirect, url_for, flash, request
from .forms import AuthLoginForm, AuthRegisterForm
from app.commons.exts import db
from app.commons.sqlModel import User
from flask_login import login_user, login_required, current_user
from datetime import timedelta
from app.utils.sendMail import sendMail

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
@auth_bp.route('/register/', methods=['GET', 'POST'])
def auth_register():
    form = AuthRegisterForm()
    if form.validate_on_submit():
        if form.confirmed.data:
            """创建用户"""
            user = User(email=form.email.data.lower(), username=form.username.data, password=form.password.data)
            user.save()
            # 邮件激活
            # 生成token
            token = user.generate_confirmation_token()
            # 将token发送给用户邮箱
            sendMail(user.email, "激活账户", 'confirm', user=user, token=token)
            flash("请通过注册邮箱激活账户!", 'info')
            return redirect(url_for('main.index'))
        else:
            """同意协议"""
            flash("请阅读同意注册协议", 'info')
            redirect(url_for('auth.auth_register'))
    return render_template('auth/register.html', form=form)

# 同意协议
@auth_bp.route('/protocol/')
def auth_protocol():
    return render_template('auth/protocol.html')


# 登录状态下,激活邮件
@auth_bp.route('/confirm/<token>')
@login_required
def auth_confirm(token):
    """通过current_user flask_login代理访问用户, 如果激活,直接跳转首页"""
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    # 如果没有激活,验证序列化内容
    if current_user.check_confirmation_token(token):
        # 设置标志位为True
        db.session.commit()
        flash('您的账户已激活.', 'success')
    else:
        flash('激活链接已过期,请重新激活.', 'warning')
    return redirect(url_for('main.index'))