import json

from flask import request
import application.round.function as RoundFuncs
from application.round import round
import service.reponse as MyResponse
from service.login import token_required


@round.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = RoundFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@round.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = RoundFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@round.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = RoundFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@round.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = RoundFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@round.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = RoundFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)
