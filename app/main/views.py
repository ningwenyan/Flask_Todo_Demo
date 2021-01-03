#!/usr/bin/env python
# coding=utf-8

from . import main_bp
from flask import render_template
from flask_login import current_user

@main_bp.route('/')
def index():
    return render_template('index.html', current_user=current_user)