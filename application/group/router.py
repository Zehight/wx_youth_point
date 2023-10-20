import json

from flask import request
import application.group.function as GroupFuncs
from application.group import group
import service.reponse as MyResponse
from service.login import token_required


@group.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = GroupFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@group.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = GroupFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@group.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = GroupFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@group.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = GroupFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@group.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = GroupFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
