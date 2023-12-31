from service.models import Learn,Action


# 新增
def create_func(**kwargs):
    learn = Learn.create(**kwargs)
    learn_id = learn['id']
    return "操作成功",learn_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    learn = Learn.get(id=kwargs['id'])
    if learn:
        learn.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    learn = Learn.get(id=kwargs['id'])
    learn.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    learn = Learn.get(id=kwargs['id'])
    result = learn.to_dict()
    result['view_num'] = Action.count(article_id = kwargs['id'])
    if learn:
        return "操作成功",result
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Learn.search(**kwargs)
    for item in result['list']:
        item['view_num'] = Action.count(article_id=item['id'])
    return "操作成功",result
