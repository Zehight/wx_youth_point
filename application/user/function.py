import json
from datetime import datetime, timedelta

import requests
from flask import request
from sqlalchemy.exc import IntegrityError
from service.models import User, Binding, Dept, File
import config

import jwt
import bcrypt

SECRET_KEY = '12dwafdsgefdsvdfgrteweddsfthrefsdvfbtrhrerdsdvbthrefdvfbthedsdvfgredsfgrds3456'


def generate_token(kwargs):
    # 设置过期时间为 48 小时后
    kwargs['pwd'] = "嘿嘿🤭，你猜？"
    payload = {
        **kwargs
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def getToken_func(**kwargs):
    open_id = kwargs['open_id']
    if open_id == '':
        return "操作失败", "非法请求"

    binding = Binding.get(open_id=open_id)

    if binding is None:
        return "操作失败", ""
    else:
        user = User.get(id=binding.user_id)
        user_info = user.to_dict()
        dept_name = ""
        avatar_name = ""
        if user.dept_id is not None:
            dept = Dept.get(id=user.dept_id)
            dept_name = dept.name

        if user.avatar is not None:
            file = File.get(id=user.avatar)
            avatar_name = file.file_name

        token = generate_token({**user_info, "dept_name": dept_name, 'avatar_name': avatar_name})
    return "操作成功", token


def register_func(**kwargs):
    if 'user_code' not in kwargs or 'real_name' not in kwargs:
        return "操作失败", "非法请求"

    user_code = kwargs['user_code']

    verify_user = User.get(user_code=user_code)
    if verify_user:
        return "操作失败", "用户已注册"

    # TODO：验证工号姓名接口，公司接口

    user = User.create(**kwargs)
    user_id = user['id']
    return "操作成功", user_id


def binding_func(**kwargs):
    if kwargs['open_id'] == '':
        return "操作失败", "非法请求"

    Binding.create(open_id=kwargs['open_id'], user_id=kwargs['user_id'])
    return "操作成功", "successful"


def update_func(**kwargs):
    user = User.get(id=kwargs['id'])
    user.update(**kwargs)
    return "操作成功", "数据修改成功"
