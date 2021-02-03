#!/usr/bin/env python
# coding=utf-8


from flask import Flask
import config
from .auth import auth_bp
from .main import main_bp
from .commons.exts import bootstrap, login_manager, db, bcrypt, csrf, mail, photos
from .commons import  commons_bp
from .utils import utils_bp
from .api.v1 import v1_bp
from .cms import cms_bp
from .api.v2 import v2_bp
from flask_uploads import patch_request_class, configure_uploads

login_manager.login_view = 'auth.auth_login'
login_manager.login_message = '欢迎来到TodoList'
#login_manager.login_view = 'cms.cms_login'
#login_manager.login_message = "欢迎访问TodoList CMS管理系统"

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 初始化插件
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    # 限制文件上传大小
    patch_request_class(app, 5*1024*1024)
    # 指定文件类型
    configure_uploads(app, photos)
    # 注册蓝图
    app.register_blueprint(auth_bp)     # 登录
    app.register_blueprint(main_bp)     # 逻辑
    app.register_blueprint(commons_bp)  # 公共
    app.register_blueprint(utils_bp)    # 工具
    app.register_blueprint(v1_bp)       # API
    app.register_blueprint(v2_bp)       # API role
    app.register_blueprint(cms_bp)      # 后台(权限控制)
    return app