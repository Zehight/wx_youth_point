from service.models import Action


# 新增
def create_func(**kwargs):
    action = Action.create(**kwargs)
    action_id = action['id']
    return "操作成功",action_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    action = Action.get(id=kwargs['id'])
    if action:
        action.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    action = Action.get(id=kwargs['id'])
    action.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    action = Action.get(id=kwargs['id'])
    if action:
        return "操作成功",action.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Action.search(**kwargs)
    return "操作成功",result
