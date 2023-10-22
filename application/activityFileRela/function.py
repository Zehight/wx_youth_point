from sqlalchemy.exc import IntegrityError
from service.models import ActivityFileRela


# 新增
def create_func(**kwargs):
    ActivityFileRela.create(**kwargs)
    return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    activityFileRela = ActivityFileRela.get(id=kwargs['id'])
    if activityFileRela:
        activityFileRela.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    activityFileRela = ActivityFileRela.get(id=kwargs['id'])
    activityFileRela.update(**kwargs)
    return "操作成功", "数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    activityFileRela = ActivityFileRela.get(id=kwargs['id'])
    if activityFileRela:
        return "操作成功",activityFileRela.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = ActivityFileRela.search(**kwargs)
    return "操作成功",result
