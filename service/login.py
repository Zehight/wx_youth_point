# import time
from functools import wraps

import jwt
from flask import request, jsonify

SECRET_KEY = '12dwafdsgefdsvdfgrteweddsfthrefsdvfbtrhrerdsdvbthrefdvfbthedsdvfgredsfgrds3456'




def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        # 获取请求头中的token
        token = request.headers.get('Authorization')

        if not token:
            # 如果请求头中不存在token，返回错误信息
            return jsonify({'message': 'Missing token'}), 401
        token = token.split(' ')[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # if payload.get('exp') < int(time.time()):
            #     return jsonify({'message': 'Token expired'}), 401
            request.token_info = payload
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            return jsonify({'message': 'Invalid token', 'code': 401})
        # 调用被装饰的函数
        return func(*args, **kwargs)

    return decorated
