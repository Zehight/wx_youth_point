import json
from datetime import datetime
from flask import request
import application.learn.function as LearnFuncs
from application.learn import learn
import service.reponse as MyResponse
from service.login import token_required


@learn.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    msg, data = LearnFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@learn.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = LearnFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@learn.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = LearnFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@learn.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = LearnFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@learn.route('/list', methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg, data = LearnFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
