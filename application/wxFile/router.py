import json
import os
from flask import request, send_from_directory, current_app,Response
import application.wxFile.function as WxFileFuncs
from application.wxFile import wxFile
from service.models import File
import service.reponse as MyResponse
from service.login import token_required
import config


@wxFile.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    requestData['create_by']=request.token_info['id']
    msg, data = WxFileFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@wxFile.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = WxFileFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@wxFile.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = WxFileFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@wxFile.route('/preview', methods=['GET'])
def preview():
    id = request.args.get('id')
    file = File.get(id = id)
    response = WxFileFuncs.client.get_object(
        Bucket=config.cos_bucket,
        Key=file.file_name,
    )
    fp = response['Body'].get_raw_stream()
    return Response(fp.read(),content_type='image/jpeg')