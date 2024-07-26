from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.models import Fill,User,Binding
from application.user import function as UserFuncs


# 新增
def create_func(**kwargs):
    kwargs['create_by'] =kwargs['open_id']
    del kwargs['open_id']
    Fill.create(**kwargs)
    return "操作成功","添加成功"

def info_func(**kwargs):
    fill = Fill.get(create_by=kwargs['open_id'])
    if fill:
        return "操作成功", fill.to_dict()
    else:
        return "操作失败", '数据不存在'

# 更新
def update_func(**kwargs):
    fill = Fill.get(create_by=kwargs['open_id'])
    del kwargs['open_id']
    fill.update(**kwargs)
    return "操作成功","数据修改成功"
