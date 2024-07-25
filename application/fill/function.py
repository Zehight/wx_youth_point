from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.models import Fill,User,Binding
from application.user import function as UserFuncs


# 新增
def create_func(**kwargs):
    kwargs['create_by'] =
    user_code = kwargs['user_code']
    real_name = kwargs['real_name']
    dept_id = kwargs['dept_id']
    open_id = kwargs['open_id']
    if open_id == '':
        return "操作失败","非法请求"

    # 获取绑定信息和用户信息
    binding = Binding.get(open_id=open_id)

    if binding:
        user = User.get(id=binding.user_id)
        Fill.create(book_name=kwargs['book_name'], create_by=user.id)
        return "操作成功", "数据添加成功"
    else:
        request_user = User.get(user_code=user_code)
        if request_user:
            return "操作失败", "用户已绑定"
        user=User.create(real_name=real_name,dept_id=dept_id,user_code=user_code)
        user_id = user['id']
        Binding.create(open_id=open_id,user_id=user_id)
        msg,data = UserFuncs.getToken_func(open_id=open_id)
        return "token",data


# 更新
def update_func(**kwargs):
    fill = Fill.get(id=kwargs['id'])
    return_time = datetime.now()
    kwargs['return_time'] = return_time
    fill.update(**kwargs)
    return "操作成功","数据修改成功"


# 分页查询列表
def getlist_func(**kwargs):
    result = Fill.search(**kwargs)
    return "操作成功",result
