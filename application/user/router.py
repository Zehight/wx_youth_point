import json

from flask import request
import application.user.function as UserFuncs
from application.user import user
import service.reponse as MyResponse
from service.login import token_required


@user.route('/add',methods=['POST'])
def add():
    requestData = json.loads(request.data)
    ip = request.headers.get('X-Forwarded-For', '')
    msg,data = UserFuncs.create_func(create_ip=ip,**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/update',methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/delete',methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/info',methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/list',methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/login',methods=['POST'])
def login():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.login_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)
