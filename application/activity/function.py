from sqlalchemy.exc import IntegrityError

from service.models import Activity,ActivityFileRela,Dept,File,User


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
    user = User.get(id=activity.create_by)
    file_list = ActivityFileRela.search(activity_id=activity.id)
    if len(file_list) > 0:
        for fileItem in file_list['list']:
            file = File.get(id=str(fileItem['file_id']))
            fileItem['file_name'] = file.file_name
    result = activity.to_dict()
    result['create_by_name'] = user.real_name
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
        user = User.get(id = item['create_by'])
        item['create_by_name'] = user.real_name
        file_list = ActivityFileRela.search(activity_id=item['id'],rows=3,page=1)
        if len(file_list)>0:
            for fileItem in file_list['list']:
                file = File.get(id=str(fileItem['file_id']))
                fileItem['file_name']  = file.file_name
        item['dept_name'] = dept.name
        item['list'] = file_list['list']
    return "操作成功",result
