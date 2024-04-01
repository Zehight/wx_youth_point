from sqlalchemy import and_

from service.models import Action, Activity,db,User,File


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

def like_me_func(**kwargs):
    items = (db.session.query(Action,Activity.title,User.nike_name,File.file_name,Activity.type,Activity.id)
             .join(Activity,Action.article_id ==Activity.id)
             .join(User,Action.create_by ==User.id)
             .join(File,User.avatar ==File.id)
             .filter(and_(
        Activity.create_by==kwargs['create_by'],Action.type==kwargs['type'])). \
        order_by(Action.create_time.desc()). \
        paginate(kwargs['page'], kwargs['rows'], error_out=False))
    db.session.close()
    result = [
        {
            **item[0].to_dict(),
            'title': item[1],
            'create_name': item[2],
            'avatar_name': item[3],
            'activity_type':item[4],
            'activity_id':item[5],
        }
        for item in items.items
    ]
    total = items.total
    return "操作成功", {
        'total': total,
        'list': result
    }