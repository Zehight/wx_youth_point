from sqlalchemy import func, and_

from service.models import Message,db,Activity,User,File,Comment


# 新增
def create_func(**kwargs):
    message = Message.create(**kwargs)
    message_id = message['id']
    return "操作成功",message_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    message = Message.get(id=kwargs['id'])
    if message:
        message.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    message = Message.get(id=kwargs['id'])
    message.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    message = Message.get(id=kwargs['id'])
    result = message.to_dict()
    if message:
        return "操作成功",result
    else:
        return "操作失败",'数据不存在'

def get_count_func(**kwargs):
    query = db.session.query(
        Message.type,
        func.count(Message.type)
    ).filter(and_(Message.look_user == kwargs['look_user'],Message.is_look == '0')).group_by(Message.type).all()
    db.session.close()
    result = {}
    for item in query:
        result[item[0]] = item[1]
    return "操作成功", result




# 分页查询列表
def getlist_func(**kwargs):
    print(kwargs)
    if(kwargs['type'] == '0'):
        query = db.session.query(Message, Activity.title,Activity.type,Comment.content, User.nike_name, File.file_name). \
            join(Activity, Message.activity_id == Activity.id). \
            join(Comment,Message.comment_id == Comment.id). \
            join(User, Message.create_by == User.id).join(File, User.avatar == File.id). \
            filter(and_(Message.look_user == kwargs['look_user'], Message.type == kwargs['type']))
        items = query.paginate(kwargs['page'], kwargs['rows'], error_out=False)
        db.session.close()
        result = [
            {
                **item[0].to_dict(),
                'title': item[1],
                'activity_type': item[2],
                'comment': item[3],
                'create_by_nike_name': item[4],
                'create_by_avatar': item[5],
            }
            for item in items.items
        ]
    else:
        query = db.session.query(Message,Activity.title,Activity.type,User.nike_name,File.file_name). \
            join(Activity,Message.activity_id == Activity.id). \
            join(User,Message.create_by == User.id).join(File,User.avatar == File.id). \
            filter(and_(Message.look_user == kwargs['look_user'] , Message.type == kwargs['type']))
        items = query.paginate(kwargs['page'], kwargs['rows'], error_out=False)
        db.session.close()
        result = [
            {
                **item[0].to_dict(),
                'title': item[1],
                'activity_type': item[2],
                'comment': '',
                'create_by_nike_name': item[3],
                'create_by_avatar': item[4],
            }
            for item in items.items
        ]
    total = items.total
    return "操作成功", {
        'page': kwargs['page'],
        'rows': kwargs['rows'],
        'total': total,
        'list': result
    }
