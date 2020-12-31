#!/usr/bin/env python
# coding=utf-8

from flask_script import Manager
from app.commons.exts import db
from flask_migrate import MigrateCommand, Migrate
from app import create_app
from app.commons.sqlModel import User

app = create_app()

# 导入Manager并绑定app
manager = Manager(app)

# 导入flaks_migrate
# Migrate 绑定app,db
Migrate(app, db)
# MigrateCommand 可以使用Alembic的命令
#

manager.add_command('db', MigrateCommand) # db是别名


# 添加开发测试账户
@manager.option('-e', '--email', dest='email')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def CMS_user(email, username, password):
    user = User.query.filter_by(email=email).filter_by(password=password).first()
    if user is not None:
        print('已有账户')
    else:
        real_user = User(email, username, password)
        real_user.save()
        print('账户已创建')

# 更新密码
@manager.option('-i', '--id', dest='id')
@manager.option('-p', '--password', dest='password')
def CMS_user_update_password(id, password):
    user = User.query.filter_by(id=id).first()
    if user is not None:
        user.password = password
        user.save()
        print("密码已经更新")
    else:
        print("账户不存在")

# 删除用户
@manager.option('-e', '--email', dest='email')
def CMS_user_delete(email):
    user = User.query.filter_by(email=email).first()
    if user is not None:
        user.delete()
        print("用户已删除")
    else:
        print('用户不存在')


if __name__  == '__main__':
    manager.run()