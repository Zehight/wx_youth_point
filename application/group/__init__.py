from flask import Blueprint

group = Blueprint('group', __name__, url_prefix='/group')

# 加载控制器
from application.group import router


