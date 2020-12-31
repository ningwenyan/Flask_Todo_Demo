#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

utils_bp = Blueprint('utils', __name__, url_prefix='/utils')

from . import sendMail