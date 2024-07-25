import json
from datetime import datetime
from flask import request
import application.fill.function as FillFuncs
from application.fill import fill
import service.reponse as MyResponse
from service.login import token_required


@fill.route('/add', methods=['POST'])
def add():
    open_id = request.headers.get("x-wx-openid", "")
    requestData = json.loads(request.data)
    requestData['open_id'] = open_id
    msg, data = FillFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@fill.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = FillFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@fill.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = FillFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)



@fill.route('/myList', methods=['POST'])
@token_required
def my_list():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = FillFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
