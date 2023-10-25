from sqlalchemy.exc import IntegrityError

from service.models import Dept


# 新增
def create_func(**kwargs):
    dept = Dept.create(**kwargs)
    dept_id = dept['id']
    return "操作成功",dept_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    dept = Dept.get(id=kwargs['id'])
    if dept:
        dept.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    dept = Dept.get(id=kwargs['id'])
    dept.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    dept = Dept.get(id=kwargs['id'])
    if dept:
        return "操作成功",dept.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Dept.search(**kwargs)
    return "操作成功",result
