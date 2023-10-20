import json

from flask import request
import application.roleFileRela.function as RoleFileRelaFuncs
from application.roleFileRela import roleFileRela
import service.reponse as MyResponse
from service.login import token_required


@roleFileRela.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = RoleFileRelaFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@roleFileRela.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = RoleFileRelaFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@roleFileRela.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = RoleFileRelaFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@roleFileRela.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = RoleFileRelaFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@roleFileRela.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = RoleFileRelaFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
