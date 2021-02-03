#!/usr/bin/env python
# coding=utf-8

import os
from flask_uploads import IMAGES

# 基本配置文件
DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# 设置主域名
SERVER_NAME = "kwenyan.online:8080"

# 设置bootstrap主题
# BOOTSTRAP_BOOTSWATCH_THEME = 'slate'


# 配置数据库
# 数据库连接
DB_URI = 'mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/flask_todo_demo'
# 指定数据库连接
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF保护
SECRET_KEY = os.urandom(10)

# 配置Flask Mail
# 设置邮箱
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USERNAME = '2@qq.com'
MAIL_PASSWORD = "imkzuyoo"
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_DEFAULT_SENDER = '2@qq.com'

# 配置json返回中文
JSON_AS_ASCII = False

# 指定文件上传
# 配置文件上传
Dir = os.path.dirname(os.path.abspath(__file__))
UPLOADED_PHOTO_DEST=Dir+'/app/upload/'
UPLOAD_PHOTO_ALLOW = IMAGES