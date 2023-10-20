import json
import os
from flask import request, send_from_directory, current_app,Response
import application.file.function as FileFuncs
from application.file import file
import service.reponse as MyResponse
from service.login import token_required
import config


@file.route('/add', methods=['POST'])
@token_required
def add():
    file = request.files['file']
    requestData = request.form.to_dict()
    create_by = request.token_info['id']
    msg, data = FileFuncs.create_func(real_file=file, create_by=create_by, **requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = FileFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = FileFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/preview', methods=['GET'])
def preview():
    id = request.args.get('id')
    size = request.args.get('size','')
    msg, data = FileFuncs.getinfo_func(id=id)
    print(data)
    fileName = data['file_name']
    small_id = data['small_id']
    key = id + '_' + fileName
    small_key = small_id + '_' + fileName
    if(size == 'small'):
        response = FileFuncs.client.get_object(
            Bucket=config.small_img_bucket_name,
            Key=small_key,
        )
    else:
        response = FileFuncs.client.get_object(
            Bucket=config.img_bucket_name,
            Key=key,
        )
    fp = response['Body'].get_raw_stream()
    return Response(fp.read(),content_type='image/jpeg')
    # return send_from_directory(os.path.join(os.path.dirname(current_app.root_path), 'files'), id + '_' + fileName)