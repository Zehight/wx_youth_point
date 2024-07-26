from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.models import Fill,User,Binding
from application.user import function as UserFuncs

import random


# 随机返回
def find_shortest_subarray(array):
    shortest_index = []  # 存储长度最短的子数组的下标
    shortest_length = float('inf')  # 最短子数组的初始长度设为无穷大

    for i in range(len(array)):
        current_length = len(array[i])

        if current_length < shortest_length:
            shortest_index = [i]
            shortest_length = current_length
        elif current_length == shortest_length:
            shortest_index.append(i)
    print(shortest_index)
    return random.choice(shortest_index)

# 数组中是否有E人
def check_mbti_not_starts_with_E(array):
    for item in array:
        if item.startswith('E'):
            return False  # 如果找到符合条件的字典项，则返回False
    return True  # 遍历完整个字典数组都没有找到满足条件的字典项，则返回True



def fenzu(mbti):
    flag = '1'
    teams=[[],[],[],[],[],[]]
    fills = Fill.get_all()
    if len(fills) == 0:
        flag = '1'
        return flag
    fills_dict = [item.to_dict() for item in fills]
    for item in fills_dict:
        teams[int(item['team'])-1].append(item['mbti'])
    if mbti[0]== 'I':
        flag = str(find_shortest_subarray(teams)+1)
        return flag
    else:
        is_all_have_E = True
        for index,team in enumerate(teams):
            if(check_mbti_not_starts_with_E(team)):
                flag=str(index+1)
                is_all_have_E = False
                break
        if(is_all_have_E):
            flag = str(find_shortest_subarray(teams) + 1)
            return flag
        else:
            return flag


# 新增
def create_func(**kwargs):
    kwargs['create_by'] =kwargs['open_id']
    del kwargs['open_id']
    Fill.create(**kwargs)
    team = fenzu(kwargs['mbti'])
    return "操作成功",team

def info_func(**kwargs):
    fill = Fill.get(create_by=kwargs['open_id'])
    if fill:
        return "操作成功", fill.to_dict()
    else:
        return "操作失败", '数据不存在'

# 更新
def update_func(**kwargs):
    fill = Fill.get(create_by=kwargs['open_id'])
    del kwargs['open_id']
    fill.update(**kwargs)
    return "操作成功","数据修改成功"
