import json

from flask import request
import application.activityFileRela.function as ActivityFileRelaFuncs
from application.activityFileRela import activityFileRela
import service.reponse as MyResponse
from service.login import token_required


@activityFileRela.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = ActivityFileRelaFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activityFileRela.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = ActivityFileRelaFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activityFileRela.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = ActivityFileRelaFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activityFileRela.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = ActivityFileRelaFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@activityFileRela.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = ActivityFileRelaFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
