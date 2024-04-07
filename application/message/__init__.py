from flask import Blueprint

message = Blueprint('message', __name__, url_prefix='/message')

# 加载控制器
from application.message import router


