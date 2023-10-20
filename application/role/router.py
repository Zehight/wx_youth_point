import json

from flask import request
import application.role.function as RoleFuncs
from application.role import role
import service.reponse as MyResponse
from service.login import token_required


@role.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = RoleFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@role.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = RoleFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@role.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = RoleFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@role.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = RoleFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@role.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = RoleFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
