from flask import Blueprint

activityFileRela = Blueprint('activityFileRela', __name__, url_prefix='/activityFileRela')

# 加载控制器
from application.activityFileRela import router


