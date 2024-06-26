from sqlalchemy import desc, func, select, text

from service.models import Debate, db


# 新增
def create_func(**kwargs):
    Debate.createByAuto(**kwargs)
    return "操作成功", 'ok'


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
    print(kwargs)
    if 'ip' not in kwargs:
        return "操作失败", '参数错误'
    # 获取某个IP最新一次投票的队伍名字和辩手名字
    team = ''
    person = ''
    point = ''
    vote_list = []
    # 子查询
    query1 = db.session.query(Debate).filter(Debate.ip == kwargs['ip'], Debate.type == '1',Debate.title==kwargs['title']).order_by(
        Debate.id.desc()).first()
    query2 = db.session.query(Debate).filter(Debate.ip == kwargs['ip'], Debate.type == '2',Debate.title==kwargs['title']).order_by(
        Debate.id.desc()).first()
    query3 = db.session.query(Debate).filter(Debate.ip == kwargs['ip'], Debate.type == '3',Debate.title==kwargs['title']).order_by(
        Debate.id.desc()).first()
    if query1 is not None:
        team = query1.to_dict()['content']

    if query2 is not None:
        person = query2.to_dict()['content']

    if query3 is not None:
        point = query3.to_dict()['content']

    sql = f'''SELECT type,
	content,
	COUNT(*) AS vote_count ,title
FROM
	debate 
WHERE
	( ip, type, id,title ) IN ( SELECT ip, type, MAX( id ),title FROM debate GROUP BY ip, type,title )
	AND title = '{kwargs['title']}'
GROUP BY
	content ,title
ORDER BY
	vote_count DESC;'''
    result = db.session.execute(text(sql))
    data = result.fetchall()
    if data is not None:
        for item in data:
            vote_list.append({"type": item[0], "content": item[1], "vote_num": item[2]})

    db.session.close()
    return "操作成功", {"team": team, "person": person,"point":point, "vote":vote_list}
    # debate = Debate.get(id=kwargs['id'])
    # if debate:
    #     return "操作成功",debate.to_dict()
    # else:
    #     return "操作失败",'数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = Debate.search_by_id(**kwargs)
    print(result)
    return "操作成功", result
