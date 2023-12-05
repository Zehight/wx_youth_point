from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased

from service.models import Comment,User,File,db


# 新增
def create_func(**kwargs):
    comment = Comment.create(**kwargs)
    comment_id = comment['id']
    return "操作成功", comment_id


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    comment = Comment.get(id=kwargs['id'])
    if comment:
        comment.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):
    comment = Comment.get(id=kwargs['id'])
    comment.update(**kwargs)
    return "操作成功", "数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    comment = Comment.get(id=kwargs['id'])
    if comment:
        return "操作成功", comment.to_dict()
    else:
        return "操作失败", '数据不存在'


def getUser(user_id):
    user = User.get(id=user_id)
    file = File.get(id=user.avatar)
    return {'nike_name':user.to_dict()['nike_name'],'avatar_name':file.file_name}

# 分页查询列表
def getlist_func(**kwargs):
    result = Comment.search(order_method='asc',**kwargs)
    for reply in result['list']:
        reply['create_by_name'] = getUser(reply['create_by'])['nike_name']
        reply['create_by_avatar_name'] = getUser(reply['create_by'])['avatar_name']
        if reply['reply_id'] is not None:
            comment = Comment.get(id = reply['reply_id'])
            reply['reply_user_name'] = getUser(comment.create_by)['nike_name']
            reply['reply_user_avatar_name'] = getUser(comment.create_by)['avatar_name']
        else:
            reply['reply_user_name'] = ''
    return "操作成功", result


def get_list_by_activity(**kwargs):
    result = Comment.search(order_method='asc',**kwargs)
    for main_reply in result['list']:
        main_reply['create_by_name'] = getUser(main_reply['create_by'])['nike_name']
        main_reply['create_by_avatar_name'] = getUser(main_reply['create_by'])['avatar_name']
        main_reply['reply_user_name'] = ''
        follow_reply_list = Comment.search(comment_main_id=main_reply['id'], page=1, rows=3)
        for follow_reply in follow_reply_list['list']:
            follow_reply['create_by_name'] = getUser(follow_reply['create_by'])['nike_name']
            follow_reply['create_by_avatar_name'] = getUser(follow_reply['create_by'])['avatar_name']
            if follow_reply['reply_id'] is not None:
                comment = Comment.get(id=follow_reply['reply_id'])
                follow_reply['reply_user_name'] = getUser(comment.create_by)['nike_name']
                follow_reply['reply_user_avatar_name'] = getUser(comment.create_by)['avatar_name']
            else:
                follow_reply['reply_user_name'] = ''

        main_reply['reply'] = follow_reply_list['list']
    return "操作成功", result

def get_not_look(**kwargs):
    CommentAlias = aliased(Comment)  # 创建一个别名
    items = db.session.query(CommentAlias).\
        join(Comment, CommentAlias.reply_id == Comment.id, isouter=True).\
        filter(Comment.create_by == kwargs['create_by'], CommentAlias.is_look == '0').\
        paginate(kwargs['page'], kwargs['rows'], error_out=False)
    result = [item.to_dict() for item in items.items]
    total = items.total
    return "操作成功", {
            'page': kwargs['page'],
            'rows': kwargs['rows'],
            'total': total,
            'list': result
        }
