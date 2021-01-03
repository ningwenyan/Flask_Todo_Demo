#!/usr/bin/env python
# coding=utf-8


from . import commons_bp
from app.utils.captcha import Captcha
from app.utils import captcha_cache
from io import BytesIO
from flask import make_response

@commons_bp.route('/graph_captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    captcha_cache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp