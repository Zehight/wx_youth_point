import json

from flask import request
import application.groupRoleRela.function as GroupRoleRelaFuncs
from application.groupRoleRela import groupRoleRela
import service.reponse as MyResponse
from service.login import token_required


@groupRoleRela.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = GroupRoleRelaFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@groupRoleRela.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = GroupRoleRelaFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@groupRoleRela.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = GroupRoleRelaFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@groupRoleRela.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = GroupRoleRelaFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@groupRoleRela.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = GroupRoleRelaFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
