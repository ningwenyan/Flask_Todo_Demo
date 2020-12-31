#!/usr/bin/env python
# coding=utf-8

from .exts import db, bcrypt, login_manager
from flask_login import UserMixin
from datetime import datetime
import enum
import re
from sqlalchemy.ext.declarative import synonym_for
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import synonym
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class BaseModel:
    """所有Model的父模板, 集成 db ORM 保存,删除属性"""

    def __commit(self):
        # __ 双下划线避免子类覆盖功能
        from sqlalchemy.exc import IntegrityError
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    def delete(self):
        # 删除数据
        db.session.delete(self)
        self.__commit()

    def save(self):
        # 添加数据
        db.session.add(self)
        self.__commit()
        return self

class GenderEnum(enum.Enum):
    MALE = 1
    FEMAle = 2
    SECRET = 3

def check_length(attribute, length):
    """检查属性值长度"""
    try:
        return bool(attribute) and len(attribute) <= length
    except:
        return False

EMAIL_REGEX = re.compile(r"^\S+@\S+\.\S+$")
USERNAME_REGEX = re.compile(r"^\S+$")
PHONE_REGEX = re.compile(r"1[3|4|5|7|8][0-9]{9}")


class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _email = db.Column(db.String(64), unique=True, index=True)  # 匹配正则
    _username = db.Column(db.String(64), unique=True, index=True) # 匹配正则
    _password_hash = db.Column(db.String(128))        # 密码加密,增强安全性, 隐藏属性值
    confirmed = db.Column(db.Boolean, default=False)  # 激活状态
    location = db.Column(db.String(64))               # 位置:北京,河北....
    about_me = db.Column(db.TEXT())                   # 自我介绍
    member_since = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间,网站全部采用UTC时间
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)     # 最后一次登录时间
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.SECRET)
    avatar = db.Column(db.String(100)) # 头像保存地址
    real_name = db.Column(db.String(64))  # 此字段用来验证 网络安全法案中的身份验证,因为是测试,而且要接入API,此处不做验证
    _phone = db.Column(db.String(11))
    birthday = db.Column(db.DateTime, default=None)

    def __init__(self, email, username, password, *args, **kwargs):
        self.email = email
        self.username = username
        self.password = password

    # -- username 正则匹配,长度约束
    @property
    def username(self):
        return  self._username

    @username.setter
    def username(self, raw_username):
        """检查有效长度"""
        is_valid_length = check_length(raw_username, 24)
        if not is_valid_length or not bool(USERNAME_REGEX.match(raw_username)):
            raise ValueError('{} 不是有效的用户名,不允许超过24位字符'.format(raw_username))
        self._username = raw_username

    username = synonym("_username", descriptor=username)

    # -- email 正则匹配
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, raw_email):
        if not check_length(raw_email, 64) or not bool(EMAIL_REGEX.match(raw_email)):
            raise ValueError("{} 不是有效的邮箱".format(raw_email))
        self._email = raw_email

    email = synonym("_email", descriptor=email)

    # -- 密码加密/解密
    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, raw_password):
        """加密密码"""
        self._password_hash = bcrypt.generate_password_hash(raw_password)

    @password.deleter
    def password(self):
        del self._password_hash

    def check_password(self, password):
        """如果原始密码和加密后的密码相同,返回True"""
        return bcrypt.check_password_hash(self._password_hash, password)

    # -- phone
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, raw_phone):
        if not check_length(raw_phone, 11) or not bool(PHONE_REGEX.match(raw_phone)):
            raise ValueError("{} 不匹配手机号".format(raw_phone))
        self._phone = raw_phone

    # -- 记录最后一次登录时间
    def seen(self):
        self.last_seen = datetime.utcnow()
        return self.save()

    def __repr__(self):
        return "<User %r>" % self.username

    # -- 创建邮箱token
    # 生成token,使用itsdangerous序列化token,确定唯一用户,并设置超时时间
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm':self.id}).decode('utf-8')

    # 接受序列化信息并检测
    def check_confirmation_token(self, token):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            # 检测唯一id
            return False
        # 所有检测通过,证明唯一用户,设置标志位
        self.confirmed = True
        # 没有执行db.session.commit(), 因为用户这里并不能确定用户点击了激活的超链接
        # 这将会在 views.py 中定义
        db.session.add(self)
        return True


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))