import json

from flask import Response


# 返回信息
def make_succ_response(code=200,data='',msg=''):
    data = json.dumps({'code': code, 'data': data,'msg':msg})
    return Response(data, mimetype='application/json')


