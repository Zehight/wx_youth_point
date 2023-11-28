from flask import Blueprint

comment = Blueprint('comment', __name__, url_prefix='/comment')

# 加载控制器
from application.comment import router


