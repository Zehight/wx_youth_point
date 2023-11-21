from flask import Blueprint

action = Blueprint('action', __name__, url_prefix='/action')

# 加载控制器
from application.action import router


