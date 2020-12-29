
#!/usr/bin/env python
# coding=utf-8

from . import commons_bp
from flask_wtf.csrf import CSRFError
from flask import render_template

@commons_bp.app_errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400