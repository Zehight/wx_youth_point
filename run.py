import json

import pymysql
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import config

from application import GATEWAY

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(GATEWAY)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(config.username, config.password,config.db_address,config.data_base)

app.config['autocommit_on_error'] = True

pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

app.config.from_object('config')


@app.route('/' + config.API_GATEWAY + '/health/check', methods=['GET'])
def check():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    return {'ip':x_forwarded_for}

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9000)


from gunicorn.app.base import BaseApplication
class GunicornApp(BaseApplication):
    def __init__(self, app):
        self.options = {
            'bind': '0.0.0.0:9000'
        }
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application


if __name__ == '__main__':
    gunicorn_app = GunicornApp(app)
    gunicorn_app.run()


