from sqlalchemy.exc import IntegrityError
from service.models import RoleFileRelation


# 新增
def create_func(**kwargs):
    roleFileRela = RoleFileRelation.create(**kwargs)
    return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    roleFileRela = RoleFileRelation.get(id=kwargs['id'])
    if roleFileRela:
        roleFileRela.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    roleFileRela = RoleFileRelation.get(id=kwargs['id'])
    if roleFileRela:
        try:
            roleFileRela.update(**kwargs)
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
    roleFileRela = RoleFileRelation.get(id=kwargs['id'])
    if roleFileRela:
        return "操作成功",roleFileRela.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = RoleFileRelation.search(**kwargs)
    return "操作成功",result
