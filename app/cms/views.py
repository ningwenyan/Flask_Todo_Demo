#!/usr/bin/env python
# coding=utf-8

from . import cms_bp
from flask import render_template, request, url_for, redirect, current_app
from .forms import CMSLoginForm, AddRoleForm
from app.commons.sqlModel import User, Role, Resource
from flask_login import login_user, current_user, login_required, logout_user
from datetime import timedelta


@cms_bp.route('/')
def index():
    return redirect(url_for('cms.cms_login'))


@cms_bp.route('/login/', methods=['GET', 'POST'])
def cms_login():
    form = CMSLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            if form.confirmed.data:
                login_user(user.seen(), remember=True, duration=timedelta(days=30))
            else:
                login_user(user.seen())
            # 判断next
            url_next = request.args.get("next")
            if url_next is None or not url_next.startswith('/'):
                url_next = url_for('cms.cms_user')
            return redirect(url_for('cms.cms_user') or url_next)
    return render_template('cms/login.html', form=form)


# 为用户赋予角色
@cms_bp.route('/user/')
@login_required
def cms_user():
    users = User.query.all()
    print(users)
    return render_template('cms/user_role.html',  users = users)

# 创建角色,并为角色赋予资源
@cms_bp.route('/role_resource/')
@login_required
def cms_role_resource():
    form = AddRoleForm()
    roles = Role.query.all()
    return render_template('cms/role_resource.html', roles = roles, form=form)


def handel_convert(seq):
    x, y = seq
    return [x.split('<')[0], y.split('<')[0]]

# 查看所有资源,并且添加某资源到数据库
@cms_bp.route('/resources/')
@login_required
def cms_resources():
    app = current_app._get_current_object()
    real_routes = [['%s' % rule, '%s' % rule.endpoint] for rule in app.url_map.iter_rules()]
    routes = list(map(handel_convert, real_routes))
    resources = Resource.query.all()
    real_resources = []
    for resource in resources:
        real_resources.append(resource.url)
    return render_template('cms/resources.html', routes = routes, real_resources= real_resources)

@cms_bp.route('/logout/')
@login_required
def cms_logout():
    logout_user()
    return redirect(url_for('auth.auth_login'))