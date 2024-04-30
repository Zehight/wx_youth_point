import json
from datetime import datetime
from flask import request
import application.debate.function as DebateFuncs
from application.debate import debate
import service.reponse as MyResponse
from service.login import token_required


@debate.route('/add', methods=['POST'])
def add():
    x_forwarded_for = request.headers.get('X-ORIGINAL-FORWARDED-FOR')
    # x_forwarded_for = '192.168.2.2'
    requestData = json.loads(request.data)
    requestData['ip'] = x_forwarded_for
    msg, data = DebateFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@debate.route('/update', methods=['POST'])
def update():
    requestData = json.loads(request.data)
    msg, data = DebateFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@debate.route('/delete', methods=['POST'])
def delete():
    requestData = json.loads(request.data)
    msg, data = DebateFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@debate.route('/info', methods=['POST'])
def info():
    x_forwarded_for = request.headers.get('X-ORIGINAL-FORWARDED-FOR')
    # x_forwarded_for = '192.168.1.1'
    requestData={}
    requestData['ip'] = x_forwarded_for
    msg, data = DebateFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@debate.route('/list', methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg, data = DebateFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
