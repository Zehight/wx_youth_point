import json
import requests
from service.models import File
import config
from service.cos_client import client



response = requests.get("http://api.weixin.qq.com/_/cos/getauth")
info=json.loads(response.text)

# 新增
def create_func(**kwargs):
    kwargs['id'] =kwargs['file_name'].split(".")[0]
    File.create(**kwargs)
    return "操作成功", "数据添加成功"

def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    file = File.get(id=kwargs['id'])
    if file:
        file.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'

def getlist_func(**kwargs):
    result = File.search(**kwargs)
    return "操作成功",result