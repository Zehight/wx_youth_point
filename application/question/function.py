from service.models import Question


# 新增
def create_func(**kwargs):
    question = Question.create(**kwargs)
    question_id = question['id']
    return "操作成功",question_id



# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    question = Question.get(id=kwargs['id'])
    if question:
        question.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    question = Question.get(id=kwargs['id'])
    question.update(**kwargs)
    return "操作成功","数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    question = Question.get(id=kwargs['id'])
    if question:
        return "操作成功",question.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Question.search(**kwargs)
    return "操作成功",result
