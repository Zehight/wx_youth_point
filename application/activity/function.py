from sqlalchemy.exc import IntegrityError

from service.models import Activity


# 新增
def create_func(**kwargs):
    activity = Activity.create(**kwargs)
    activity_id = activity.id
    return "操作成功",activity_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    activity = Activity.get(id=kwargs['id'])
    if activity:
        activity.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    activity = Activity.get(id=kwargs['id'])
    activity.update(**kwargs)
    activity_new = Activity.get(id=kwargs['id'])
    return "操作成功",activity_new.to_dict()


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    activity = Activity.get(id=kwargs['id'])
    if activity:
        return "操作成功",activity.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Activity.search(**kwargs)
    return "操作成功",result
