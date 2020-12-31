#!/usr/bin/env python
# coding=utf-8

import os

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
MAIL_USERNAME = '@qq.com'
MAIL_PASSWORD = "imkzuyoomffddijc"
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_DEFAULT_SENDER = '@qq.com'