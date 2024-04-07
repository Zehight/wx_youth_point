import json
from datetime import datetime
from flask import request
import application.message.function as MessageFuncs
from application.message import message
import service.reponse as MyResponse
from service.login import token_required


@message.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    msg, data = MessageFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@message.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = MessageFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@message.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = MessageFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@message.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = MessageFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)

@message.route('/count', methods=['POST'])
@token_required
def count():
    requestData = {}
    requestData['look_user'] = request.token_info['id']
    msg, data = MessageFuncs.get_count_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@message.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    requestData['look_user'] = request.token_info['id']
    msg, data = MessageFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
