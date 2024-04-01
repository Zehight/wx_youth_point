import json
from datetime import datetime
from flask import request
import application.action.function as ActionFuncs
from application.action import action
import service.reponse as MyResponse
from service.login import token_required


@action.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = ActionFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@action.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = ActionFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@action.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = ActionFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@action.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = ActionFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@action.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = ActionFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)

@action.route('/message', methods=['POST'])
@token_required
def like_me():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = ActionFuncs.like_me_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
