from sqlalchemy.exc import IntegrityError
from service.models import GroupRoleRelation
from application.roleFileRela import function as RoleFileRelaFuncs


# 新增
def create_func(**kwargs):
    GroupRoleRelation.create(**kwargs)
    return "操作成功","角色投入完成"


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    groupRoleRela = GroupRoleRelation.get(id=kwargs['id'])
    if groupRoleRela:
        groupRoleRela.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    groupRoleRela = GroupRoleRelation.get(id=kwargs['id'])
    if groupRoleRela:
        try:
            groupRoleRela.update(**kwargs)
            return "操作成功","数据修改成功"
        except IntegrityError as e:
            print(e)
            if 'Duplicate entry' in str(e):
                return "操作失败","数据信息重复"
            else:
                return "操作失败","服务器错误"
    else:
        return "操作失败",'数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    groupRoleRela = GroupRoleRelation.get(id=kwargs['id'])
    if groupRoleRela:
        return "操作成功",groupRoleRela.to_dict()

    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = GroupRoleRelation.search(**kwargs)
    return "操作成功",result
