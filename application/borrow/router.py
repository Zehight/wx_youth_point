import json
from datetime import datetime
from flask import request
import application.borrow.function as BorrowFuncs
from application.borrow import borrow
import service.reponse as MyResponse
from service.login import token_required


@borrow.route('/add', methods=['POST'])
def add():
    open_id = request.headers.get("x-wx-openid", "")
    requestData = json.loads(request.data)
    requestData['open_id'] = open_id
    if 'user_code' not in requestData or 'real_name' not in requestData:
        return MyResponse.make_succ_response(msg='请求失败', data="表单不完整")
    msg, data = BorrowFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@borrow.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = BorrowFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@borrow.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = BorrowFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)



@borrow.route('/myList', methods=['POST'])
@token_required
def my_list():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = BorrowFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
