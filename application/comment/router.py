import json
from datetime import datetime
from flask import request
import application.comment.function as CommentFuncs
from application.comment import comment
import service.reponse as MyResponse
from service.login import token_required


@comment.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = CommentFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = CommentFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = CommentFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = CommentFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    requestData['is_delete'] = '0'
    msg, data = CommentFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/list_by_activity', methods=['POST'])
@token_required
def list_by_activity():
    requestData = json.loads(request.data)
    requestData['is_delete'] = '0'
    msg, data = CommentFuncs.get_list_by_activity(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/list_by_not_look', methods=['POST'])
@token_required
def list_by_not_look():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = CommentFuncs.get_not_look(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@comment.route('/list_by_my_comment', methods=['POST'])
@token_required
def list_by_my_comment():
    requestData = json.loads(request.data)
    requestData['create_by'] = request.token_info['id']
    msg, data = CommentFuncs.get_my_comment_look(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)

