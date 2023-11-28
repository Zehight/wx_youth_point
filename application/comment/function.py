from sqlalchemy.exc import IntegrityError

from service.models import Comment


# 新增
def create_func(**kwargs):
    comment = Comment.create(**kwargs)
    comment_id = comment['id']
    return "操作成功",comment_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    comment = Comment.get(id=kwargs['id'])
    if comment:
        comment.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    comment = Comment.get(id=kwargs['id'])
    comment.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    comment = Comment.get(id=kwargs['id'])
    if comment:
        return "操作成功",comment.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Comment.search(**kwargs)
    return "操作成功",result
