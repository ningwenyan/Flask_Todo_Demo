#!/usr/bin/env python
# coding=utf-8


from flask import Flask
import config
from .auth import auth_bp
from .main import main_bp
from .commons.exts import bootstrap, login_manager, db, bcrypt, csrf
from .commons import  commons_bp


login_manager.login_view = 'auth.auth_login'
login_manager.login_message = '欢迎来到TodoList'

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 初始化插件
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    # 注册蓝图
    app.register_blueprint(auth_bp)     # 登录
    app.register_blueprint(main_bp)     # 逻辑
    app.register_blueprint(commons_bp)  # 公共

    return app