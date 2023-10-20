from sqlalchemy.exc import IntegrityError

from service.login import token_required
from service.models import Group
from application.groupRoleRela import function as GroupRoleRelaFuncs
from application.role import function as RoleFuncs


# 新增
def create_func(**kwargs):
    group = Group.create(**kwargs)
    return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    group = Group.get(id=kwargs['id'])
    if group:
        group.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    group = Group.get(id=kwargs['id'])
    if group:
        try:
            group.update(**kwargs)
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
    group = Group.get(id=kwargs['id'])
    if group:
        group_dict = group.to_dict()
        res = GroupRoleRelaFuncs.getlist_func(group_id = group_dict['id'])[1]
        role_list = []
        for item in res['list']:
            role_info = RoleFuncs.getinfo_func(id=item['role_id'])[1]
            if not isinstance(role_info, str):
                role_list.append({**role_info, 'group_role_rela_id': item['id']})
        return "操作成功", {**group_dict,"role_list":role_list,"total":res['total']}
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Group.search(**kwargs)
    return "操作成功",result
