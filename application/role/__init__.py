from flask import Blueprint

role = Blueprint('role', __name__, url_prefix='/role')

# 加载控制器
from application.role import router


