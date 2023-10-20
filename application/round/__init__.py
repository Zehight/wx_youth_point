from flask import Blueprint

round = Blueprint('round', __name__, url_prefix='/round')

# 加载控制器
from application.round import router


