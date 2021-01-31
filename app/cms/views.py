#!/usr/bin/env python
# coding=utf-8

from . import cms_bp


@cms_bp.route('/addRole/')
def add_role():
    return '1'