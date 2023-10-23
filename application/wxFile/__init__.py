from flask import Blueprint

wxFile = Blueprint('wxFile', __name__, url_prefix='/wxFile')

# 加载控制器
from application.wxFile import router


