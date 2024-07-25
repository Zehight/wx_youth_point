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


@fill.route('/info', methods=['POST'])
def update():
    open_id = request.headers.get("x-wx-openid", "")
    requestData = json.loads(request.data)
    requestData['open_id'] = open_id
    msg, data = FillFuncs.info_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@fill.route('/update', methods=['POST'])
def update():
    open_id = request.headers.get("x-wx-openid", "")
    requestData = json.loads(request.data)
    requestData['open_id'] = open_id
    msg, data = FillFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)