from flask import Blueprint
import config

GATEWAY = Blueprint(config.API_GATEWAY, __name__, url_prefix='/' + config.API_GATEWAY)

# 注册蓝图
from application.activity import activity
from application.round import round
from application.group import group
from application.role import role
from application.groupRoleRela import groupRoleRela
from application.roleFileRela import roleFileRela
from application.user import user
from application.file import file

GATEWAY.register_blueprint(activity)
GATEWAY.register_blueprint(round)
GATEWAY.register_blueprint(group)
GATEWAY.register_blueprint(role)
GATEWAY.register_blueprint(groupRoleRela)
GATEWAY.register_blueprint(roleFileRela)
GATEWAY.register_blueprint(user)
GATEWAY.register_blueprint(file)