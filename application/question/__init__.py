from flask import Blueprint

question = Blueprint('question', __name__, url_prefix='/question')

# 加载控制器
from application.question import router


