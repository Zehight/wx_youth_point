from flask import Blueprint

power = Blueprint('power', __name__, url_prefix='/power')

# 加载控制器
from application.power import router


