import json
from datetime import datetime, timedelta

import requests
from sqlalchemy.exc import IntegrityError
from service.models import User,WxLogin
import config

import jwt
import bcrypt

SECRET_KEY = '12dwafdsgefdsvdfgrteweddsfthrefsdvfbtrhrerdsdvbthrefdvfbthedsdvfgredsfgrds3456'


# 新增
def create_func(**kwargs):
    if 'email' not in kwargs or kwargs['create_ip'] is '':
        return "操作失败", "服务器错误"
    email_user = User.get(email=kwargs['email'])

    ip_user = User.get(create_ip=kwargs['create_ip'])
    if email_user or ip_user:
        return "操作失败", "数据信息重复或注册数量达到上限"
    else:
        if(len(kwargs['pwd'])<8):
            return '操作失败','密码需要大于8位'

        else:
            kwargs['pwd'] = bcrypt.hashpw(kwargs['pwd'].encode(), bcrypt.gensalt())
            User.create(**kwargs)
        return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    user = User.get(id=kwargs['id'])
    if user:
        user.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):

    user = User.get(id=kwargs['id'])
    if user:
        try:
            user.update(**kwargs)
            return "操作成功", "数据修改成功"
        except IntegrityError as e:
            print(e)
            if 'Duplicate entry' in str(e):
                return "操作失败", "数据信息重复"
            else:
                return "操作失败", "服务器错误"
    else:
        return "操作失败", '数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    user = User.get(id=kwargs['id'])
    if user:
        return "操作成功", user.to_dict()
    else:
        return "操作失败", '数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = User.search(**kwargs)
    return "操作成功", result


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


def login_func(**kwargs):
    if 'js_code' in kwargs:
        res = requests.get(url='https://api.weixin.qq.com/sns/jscode2session', params={
            'appid': config.app_id,
            'secret': config.app_secret,
            'js_code': kwargs['js_code'],
            'grant_type': 'authorization_code'
        })
        open_id = json.loads(res.text)['openid']
        wx_user = WxLogin.get(open_id = open_id)
        if wx_user is None:
            return "操作失败", "微信用户未登录"
        else:
            user = User.get(id=wx_user.to_dict()['user_id'])
    else:
        user = User.get(email=kwargs['email'])
    if user:
        if bcrypt.checkpw(kwargs['pwd'].encode(), user.pwd.encode()):
            token = generate_token(user.to_dict())
            return "操作成功",token
        else:
            return "操作失败", "错误的用户名或密码"
    else:
        return "操作失败", "错误的用户名或密码"

# def wx_login_func(**kwargs):
