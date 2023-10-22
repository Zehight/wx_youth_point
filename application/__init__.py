from flask import Blueprint
import config

GATEWAY = Blueprint(config.API_GATEWAY, __name__, url_prefix='/' + config.API_GATEWAY)

# 注册蓝图
from application.user import user
from application.file import file
from application.activity import activity
from application.dept import dept
from application.activityFileRela import activityFileRela

GATEWAY.register_blueprint(user)
GATEWAY.register_blueprint(file)
GATEWAY.register_blueprint(activity)
GATEWAY.register_blueprint(dept)
GATEWAY.register_blueprint(activityFileRela)