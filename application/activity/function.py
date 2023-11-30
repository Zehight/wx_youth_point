from sqlalchemy.exc import IntegrityError

from service.models import Activity, ActivityFileRela, Dept, File, User, Action


# 新增
def create_func(**kwargs):
    activity = Activity.create(**kwargs)
    activity_id = activity['id']
    return "操作成功", activity_id


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    activity = Activity.get(id=kwargs['id'])
    if activity:
        activity.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):
    activity = Activity.get(id=kwargs['id'])
    activity.update(**kwargs)
    return "操作成功", "数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    activity = Activity.get(id=kwargs['id'])

    dept = Dept.get(id=activity.dept_id)
    user = User.get(id=activity.create_by)
    file_list = ActivityFileRela.search(activity_id=activity.id)

    # 点赞，收藏，查看
    view_num = Action.count(article_id=kwargs['id'])
    ActionRes = Action.search(article_id=kwargs['id'], create_by=kwargs['create_by'])
    ActionList = ActionRes['list']
    collection = sum(1 for d in ActionList if d.get('type') == '1')
    like = sum(1 for d in ActionList if d.get('type') == '2')

    if file_list['total'] > 0:
        for fileItem in file_list['list']:
            file = File.get(id=str(fileItem['file_id']))
            fileItem['file_name'] = file.file_name
    result = activity.to_dict()
    result['create_by_name'] = user.real_name
    result['dept_name'] = dept.name
    result['view_num'] = view_num
    result['collection'] = collection
    result['like'] = like
    result['list'] = file_list['list']
    if activity:
        return "操作成功", result
    else:
        return "操作失败", '数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    create_by = kwargs['create_by']
    del kwargs['create_by']
    result = Activity.search(**kwargs)
    for item in result['list']:
        dept = Dept.get(id=item['dept_id'])
        user = User.get(id=item['create_by'])
        item['create_by_name'] = user.real_name

        # 点赞，收藏，查看
        item['view_num'] = Action.count(article_id=item['id'])
        ActionRes = Action.search(article_id=item['id'], create_by=create_by)
        ActionList = ActionRes['list']
        item['collection'] = sum(1 for d in ActionList if d.get('type') == '1')
        item['like'] = sum(1 for d in ActionList if d.get('type') == '2')

        file_list = ActivityFileRela.search(activity_id=item['id'], rows=3, page=1)
        if file_list['total'] > 0:
            for fileItem in file_list['list']:
                file = File.get(id=str(fileItem['file_id']))
                fileItem['file_name'] = file.file_name
        item['dept_name'] = dept.name
        item['list'] = file_list['list']
    return "操作成功", result

def getLearn_func():
    result1 = Activity.search(type="学习",block="思想引领",page=1,rows=5)
    result2 = Activity.search(type="学习",block="业务知识",page=1,rows=5)
    result3 = Activity.search(type="学习",block="团务百科",page=1,rows=5)
    result4 = Activity.search(type="学习",block="主题活动",page=1,rows=5)
    result = [{"name":"思想引领","list":result1['list']},{"name":"业务知识","list":result2['list']},{"name":"团务百科","list":result3['list']},{"name":"主题活动","list":result4['list']}]
    return "操作成功",{"total":20,"result":result}