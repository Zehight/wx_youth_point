from sqlalchemy.exc import IntegrityError

from service.login import token_required
from service.models import Activity
from application.round import function as RoundFuncs


# 新增
def create_func(**kwargs):
    activity = Activity.create(**kwargs)
    return "操作成功",1


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
    if activity:
        try:
            activity.update(**kwargs)
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
    activity = Activity.get(id=kwargs['id'])
    if activity:
        activity_dict = activity.to_dict()
        round_res = RoundFuncs.getlist_func(activity_id = activity_dict['id'])[1]
        round_list = []
        for item in round_res['list']:
            round_info = RoundFuncs.getinfo_func(id = item['id'])[1]
            if not isinstance(round_info, str):
                round_list.append({**round_info, 'group_role_rela_id': item['id']})
        return "操作成功",{"round_list":round_list,**activity_dict,"total":round_res['total']}
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Activity.search(**kwargs)
    return "操作成功",result
