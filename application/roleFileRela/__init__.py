from flask import Blueprint

roleFileRela = Blueprint('roleFileRela', __name__, url_prefix='/roleFileRela')

# 加载控制器
from application.roleFileRela import router


