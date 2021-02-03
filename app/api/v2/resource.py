#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from flask import request, jsonify, current_app, url_for
from app.commons.sqlModel import Resource as RResource, Role

class GetAllResource(Resource):
    def get(self):
        resources = RResource.query.all()
        real_resources = []
        for resource in resources:
            real_resources.append([resource.name, resource.url])
        to_dict = {
            'resources': real_resources
        }
        return jsonify(to_dict)

    def post(self):
        resource = RResource(request.json.get('name'), request.json.get('url'))
        resource.save()
        resources = RResource.query.all()
        real_resources = []
        for resource in resources:
            real_resources.append([resource.name, resource.url])
        to_dict = {
            'resources': real_resources
        }
        return jsonify(to_dict)

class UpdateRoleResource(Resource):
    def get(self, id):
        role = Role.query.get_or_404(id)
        if role is not None:
            resources =[resource.name for resource in role.resources]
            to_dict = {
                'role_id': role.id,
                'resources' : resources
            }
            return jsonify(to_dict)

    def post(self, id):
        role = Role.query.get_or_404(id)
        if role is not None and request.json.get('resources'):
            print(request.json.get('resources'))
            real_resources = [ resource.strip() for resource in request.json.get('resources')]
            role_resource = []
            for resource in real_resources:
                if RResource.query.filter_by(name=resource).first() is not None:
                    real_resource = RResource.query.filter_by(name=resource).first()
                    role_resource.append(real_resource)
            role.resources = role_resource
            role.save()
            resources = [resource.name for resource in role.resources]
            to_dict = {
                'role_id': role.id,
                'resources' : resources
            }
            return jsonify(to_dict)

def handel_convert(seq):
    x, y = seq
    return [x.split('<')[0], y.split('<')[0]]


class GetURLMap(Resource):
    def get(self):
        app = current_app._get_current_object()
        # links = []
        # for rule in app.url_map.iter_rules():
        #     print(rule.arguments)
        #     print(rule)
        #     print(rule.endpoint)
        #
        #     links.append([rule])
        # print(links)
        real_routes = [['%s' % rule, '%s' % rule.endpoint] for rule in app.url_map.iter_rules()]
        routes = list(map(handel_convert, real_routes))
        to_dict = {
            'map': routes
        }
        return jsonify(to_dict)
