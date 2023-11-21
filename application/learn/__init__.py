from flask import Blueprint

learn = Blueprint('learn', __name__, url_prefix='/learn')

# 加载控制器
from application.learn import router


