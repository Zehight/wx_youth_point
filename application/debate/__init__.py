from flask import Blueprint

debate = Blueprint('debate', __name__, url_prefix='/debate')

# 加载控制器
from application.debate import router


