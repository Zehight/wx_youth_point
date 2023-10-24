import json
from datetime import datetime, timedelta

import requests
from flask import request
from sqlalchemy.exc import IntegrityError
from service.models import User,Binding,Dept
import config

import jwt
import bcrypt

SECRET_KEY = '12dwafdsgefdsvdfgrteweddsfthrefsdvfbtrhrerdsdvbthrefdvfbthedsdvfgredsfgrds3456'



def generate_token(kwargs):
    # 设置过期时间为 48 小时后
    expire_time = datetime.utcnow() + timedelta(hours=48)
    kwargs['pwd']="嘿嘿🤭，你猜？"
    payload = {
        **kwargs,
        'exp': expire_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def getToken_func(**kwargs):
    open_id = kwargs['open_id']
    if open_id == '':
        return "操作失败", "非法请求"

    binding = Binding.get(open_id=open_id)

    if binding is None:
        return "操作失败",""
    else:
        user = User.get(id = binding.user_id)
        user_info = user.to_dict()
        dept_name = ""
        if user.dept_id is not None:
            dept = Dept.get(id = user.dept_id)
            dept_name = dept.name

        token = generate_token({**user_info,"dept_name":dept_name})
    return "操作成功",token
    #     wx_user = WxLogin.get(open_id = open_id)
    #     if wx_user is None:
    #         return "操作失败", "微信用户未登录"
    #     else:
    #         user = User.get(id=wx_user.to_dict()['user_id'])
    # else:
    #     user = User.get(email=kwargs['email'])
    # if user:
    #     if bcrypt.checkpw(kwargs['pwd'].encode(), user.pwd.encode()):
    #         token = generate_token(user.to_dict())
    #         return "操作成功",token
    #     else:
    #         return "操作失败", "错误的用户名或密码"
    # else:
    #     return "操作失败", "错误的用户名或密码"

# def binding_func(**kwargs):
#     binding = Binding.create(**kwargs)


def register_func(**kwargs):
    if 'user_code' not in kwargs or 'real_name' not in kwargs:
        return "操作失败","非法请求"

    user_code = kwargs['user_code']

    verify_user = User.get(user_code = user_code)
    if verify_user:
        return "操作失败","用户已注册"

    # TODO：验证工号姓名接口，公司接口

    user = User.create(**kwargs)
    user_id = user.id
    return "操作成功",user_id


def binding_func(**kwargs):
    if kwargs['open_id'] == '':
        return "操作失败","非法请求"

    Binding.create(open_id = kwargs['open_id'],user_id = kwargs['user_id'])
    return "操作成功","successful"

