from service.models import Action, Activity


# 新增
def create_func(**kwargs):
    action = Action.create(**kwargs)
    action_id = action['id']
    return "操作成功", action_id


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    action = Action.get(id=kwargs['id'])
    if action:
        action.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):
    action = Action.get(id=kwargs['id'])
    action.update(**kwargs)
    return "操作成功", "数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    action = Action.get(id=kwargs['id'])
    if action:
        return "操作成功", action.to_dict()
    else:
        return "操作失败", '数据不存在'


def get_latest_records(records):
    activity_dict = {}
    for record in records:
        article_id = record['article_id']
        if article_id not in activity_dict or activity_dict[article_id]['create_time'] < record['create_time']:
            activity_dict[article_id] = record
    return list(activity_dict.values())


# 分页查询列表
def getlist_func(**kwargs):
    result = Action.search(**kwargs)
    result['list'] = get_latest_records(result['list'])
    for item in result['list']:
        articleInfo = Activity.get(id=item['article_id'])
        if(articleInfo):
            articleInfoDict = articleInfo.to_dict()
            articleInfoDict['action_id'] = item['id']
            articleInfoDict['action_type'] = item['type']
            articleInfoDict['action_time'] = item['create_time']
            articleInfoDict['action_user'] = item['create_by']
            result['list'][result['list'].index(item)] = articleInfoDict
        else:
            result['list'][result['list'].index(item)] = {}
    return "操作成功", result

