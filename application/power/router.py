import json
from flask import request, jsonify

from application.power import power
from application.power import function as PowerFuncs


@power.route('/streamAnswer', methods=['POST'])
def test_chat():
    requestData = json.loads(request.data)
    result = PowerFuncs.streamAnswer(requestData['question'])
    return jsonify(result)


@power.route('/getStreamAnswer', methods=['POST'])
def get_chat():
    requestData = json.loads(request.data)
    result = PowerFuncs.getStreamAnswer(requestData['id'])
    return jsonify(result)
