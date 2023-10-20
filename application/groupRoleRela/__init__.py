from flask import Blueprint

groupRoleRela = Blueprint('groupRoleRela', __name__, url_prefix='/groupRoleRela')

# 加载控制器
from application.groupRoleRela import router


