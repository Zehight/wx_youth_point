import json
import uuid
import requests

answers = {}

def genStreamAnswer(question, id):
    answers[id] = ''
    payload = json.dumps({
        "messages": question
    })
    response = requests.post(f"https://gpt.miragari.com/pro/stream/ask",payload,stream=True)
    for chunk in response.iter_lines():
        chunkStr = chunk.decode('utf-8')
        if chunkStr.startswith('data: {'):
            chunkJson = json.loads(chunkStr[6:])
            print(chunkJson)
            if type(chunkJson) == dict:
                chunkRes = chunkJson['choices'][0]['delta']
                if chunkJson['choices'][0]['finish_reason'] == 'stop':
                    answers[id] = '完成：'+answers[id]
                if 'content' in chunkRes and 'role' not in chunkRes:
                    answers[id] += chunkRes['content']


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



