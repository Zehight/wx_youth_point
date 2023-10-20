from sqlalchemy.exc import IntegrityError
from service.models import Role
from application.roleFileRela import function as RoleFileRelaFuncs
from application.groupRoleRela import function as GroupRoleRelaFuncs


# 新增
def create_func(**kwargs):
    if('zone' in kwargs):
        if(len(kwargs['zone'])>1):
            return "操作失败", '请重试'
    Role.create(**kwargs)
    return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    role = Role.get(id=kwargs['id'])
    if role:
        file_list = RoleFileRelaFuncs.getlist_func(role_id = role.id)
        for item in file_list[1]['list']:
            RoleFileRelaFuncs.delete_func(id=item['id'])
        role_in_group_list = GroupRoleRelaFuncs.getlist_func(role_id = role.id)
        for item in role_in_group_list[1]['list']:
            GroupRoleRelaFuncs.delete_func(id=item['id'])
        role.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    role = Role.get(id=kwargs['id'])
    if role:
        try:
            role.update(**kwargs)
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
    role = Role.get(id=kwargs['id'])

    if role:
        role_dict = role.to_dict()
        res = RoleFileRelaFuncs.getlist_func(role_id = role_dict['id'])[1]
        file_list = res['list']
        return "操作成功", {**role_dict,"file_list":file_list,"total":res['total']}

    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Role.search(**kwargs)
    result['list'] = [getinfo_func(id=item['id'])[1] for item in result['list']]
    return "操作成功",result
