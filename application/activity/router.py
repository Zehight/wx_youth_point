import json
from datetime import datetime
from flask import request
import application.activity.function as ActivityFuncs
from application.activity import activity
import service.reponse as MyResponse
from service.login import token_required


@activity.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    dept_id = request.token_info['dept_id']
    msg, data = ActivityFuncs.create_func(create_by=create_by,dept_id=dept_id,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/info', methods=['POST'])
@token_required
def info():
    create_by = request.token_info['id']
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.getinfo_func(**requestData,create_by=create_by)
    return MyResponse.make_succ_response(msg=msg, data=data)



@activity.route('/list', methods=['POST'])
@token_required
def list():
    create_by = request.token_info['id']
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.getlist_func(**requestData,create_by=create_by)
    return MyResponse.make_succ_response(msg=msg, data=data)
