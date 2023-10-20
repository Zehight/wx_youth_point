from flask import Blueprint

file = Blueprint('file', __name__, url_prefix='/file')

# 加载控制器
from application.file import router


