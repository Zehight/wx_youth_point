from sqlalchemy import desc, func, select, text

from service.models import Debate, db


# 新增
def create_func(**kwargs):
    debate = Debate.create(**kwargs)
    debate_id = debate['id']
    return "操作成功", debate_id


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    debate = Debate.get(id=kwargs['id'])
    if debate:
        debate.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):
    debate = Debate.get(id=kwargs['id'])
    debate.update(**kwargs)
    return "操作成功", "数据修改成功"


# 查询
def getinfo_func(**kwargs):
    if 'ip' not in kwargs:
        return "操作失败", '参数错误'
    # 获取某个IP最新一次投票的队伍名字和辩手名字

    team = ''
    person = ''
    vote_list = []

    # 子查询
    query1 = db.session.query(Debate).filter(Debate.ip == kwargs['ip'], Debate.type == '1').order_by(
        Debate.create_time.desc()).first()
    query2 = db.session.query(Debate).filter(Debate.ip == kwargs['ip'], Debate.type == '2').order_by(
        Debate.create_time.desc()).first()
    if query1 is not None:
        team = query1.to_dict()['content']

    if query2 is not None:
        person = query2.to_dict()['content']

        sql = '''SELECT type,
	content,
	COUNT(*) AS vote_count 
FROM
	debate 
WHERE
	( ip, type, id ) IN ( SELECT ip, type, MAX( id ) FROM debate GROUP BY ip, type ) 
GROUP BY
	content 
ORDER BY
	vote_count DESC;'''
        result = db.session.execute(text(sql))
        data = result.fetchall()
        vote_list = []
        if data is not None:
            for item in data:
                vote_list.append({"type": item[0], "content": item[1], "vote_num": item[2]})

    db.session.close()
    return "操作成功", {"team": team, "person": person, "vote": vote_list}
    # debate = Debate.get(id=kwargs['id'])
    # if debate:
    #     return "操作成功",debate.to_dict()
    # else:
    #     return "操作失败",'数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = Debate.search(**kwargs)
    return "操作成功", result
