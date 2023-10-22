from flask import Blueprint

dept = Blueprint('dept', __name__, url_prefix='/dept')

# 加载控制器
from application.dept import router


