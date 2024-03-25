import json
import uuid
import requests
import re
import code
answers = {}

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=P9rOek0jMTCDYKH2aTrtLf7Q&client_secret=lnIqB5SfNWz4excOO01JATLekRUyNkSK"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def genStreamAnswer(question, id):
    answers[id] = ''
    payload = json.dumps({
        "messages": question,
        "stream": True
    })
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    response = requests.post(url,payload,stream=True)
    for chunk in response.iter_lines():
        chunkStr = chunk.decode('utf-8')
        if chunkStr.startswith('data: {'):
            # chunkJson = json.loads(chunkStr[6:])
            regex = re.compile(r'"result":"(.*?)"')
            result = re.findall(regex,chunkStr)
            if len(result) >0:
                 answers[id] += result[0]
    answers[id] = '完成：' + answers[id]
            # if type(chunkJson) == dict:
            #     chunkRes = chunkJson['choices'][0]['delta']
            #     if chunkJson['choices'][0]['finish_reason'] == 'stop':
            #         answers[id] = '完成：'+answers[id]
            #     if 'content' in chunkRes and 'role' not in chunkRes:
            #         answers[id] += chunkRes['content']


import threading


def streamAnswer(question):
    id = str(uuid.uuid4()).replace("-","")
    threading.Thread(target=genStreamAnswer, args=(question, id)).start()
    # 返回结果
    return {'id': id}


def getStreamAnswer(id):
    # 返回结果
    if id not in answers:
        return {'result': ''}
    result = answers[id]
    if result.startswith('完成：'):
        del answers[id]
    return {'result': result}