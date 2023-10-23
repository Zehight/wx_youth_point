from sqlalchemy.exc import IntegrityError

from service.models import Activity,ActivityFileRela,Dept


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
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    activity = Activity.get(id=kwargs['id'])
    dept = Dept.get(id=activity.dept_id)
    file_list = ActivityFileRela.search(activity_id=activity.id)
    result = activity.to_dict()
    result['dept_name'] = dept.name
    result['list'] = file_list['list']
    if activity:
        return "操作成功",result
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Activity.search(**kwargs)
    for item in result['list']:
        dept = Dept.get(id=item['dept_id'])
        file_list = ActivityFileRela.search(activity_id=item['id'])
        item['dept_name'] = dept.name
        item['list'] = file_list['list']
    return "操作成功",result
