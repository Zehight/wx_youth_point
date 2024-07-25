from flask import Blueprint

fill = Blueprint('fill', __name__, url_prefix='/fill')

# 加载控制器
from application.fill import router


