from sqlalchemy.exc import IntegrityError

from service.login import token_required
from service.models import Round
from application.group import function as GroupFuncs


# 新增
def create_func(**kwargs):
    round = Round.create(**kwargs)
    return "操作成功",1


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    round = Round.get(id=kwargs['id'])
    if round:
        round.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    round = Round.get(id=kwargs['id'])
    if round:
        try:
            round.update(**kwargs)
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
    round = Round.get(id=kwargs['id'])
    if round:
        round_dict = round.to_dict()
        group_res = GroupFuncs.getlist_func(round_id = round_dict['id'])[1]
        group_list = []
        for item in group_res['list']:
            group_info = GroupFuncs.getinfo_func(id = item['id'])[1]
            if not isinstance(group_info, str):
                group_list.append({**group_info, 'group_role_rela_id': item['id']})

        return "操作成功", {**round_dict,"group_list":group_list,"total":group_res['total']}
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Round.search(**kwargs)
    return "操作成功",result
