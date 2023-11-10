import json
from datetime import datetime
from flask import request
import application.question.function as QuestionFuncs
from application.question import question
import service.reponse as MyResponse
from service.login import token_required


@question.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    msg, data = QuestionFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@question.route('/update', methods=['POST'])
def update():
    requestData = json.loads(request.data)
    msg, data = QuestionFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@question.route('/delete', methods=['POST'])
def delete():
    requestData = json.loads(request.data)
    msg, data = QuestionFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@question.route('/info', methods=['POST'])
def info():
    requestData = json.loads(request.data)
    msg, data = QuestionFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@question.route('/list', methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg, data = QuestionFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)
