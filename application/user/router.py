import json

from flask import request
import application.user.function as UserFuncs
from application.user import user
import service.reponse as MyResponse
from service.login import token_required

@user.route('/getToken',methods=['POST'])
def login():
    open_id = request.headers.get('x-wx-openid','')
    msg,data = UserFuncs.getToken_func(open_id=open_id)
    return MyResponse.make_succ_response(msg=msg,data = data)


@user.route('/register',methods=['POST'])
def register():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.register_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/binding',methods=['POST'])
def binding():
    open_id = request.headers.get("x-wx-openid","")
    requestData = json.loads(request.data)
    msg,data = UserFuncs.binding_func(open_id=open_id,**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)


@user.route('/update',methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.update(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)