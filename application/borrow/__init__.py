from flask import Blueprint

borrow = Blueprint('borrow', __name__, url_prefix='/borrow')

# 加载控制器
from application.borrow import router


