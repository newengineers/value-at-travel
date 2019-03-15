from flask import Flask

from portal.controllers.controller_ajax import ajax_controller
from .controllers.controller_account import account_controller
from .controllers.controller_api import api_controller
from .controllers.controller_main import main_controller

app = Flask(__name__,
            static_url_path='/frontend',
            static_folder='frontend',
            template_folder='frontend')
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = b'da39a3ee5e6b4b0d3255beef95601890afd80709'

app.register_blueprint(main_controller, url_prefix='/')
app.register_blueprint(account_controller, url_prefix='/account')
app.register_blueprint(api_controller, url_prefix='/api')
app.register_blueprint(ajax_controller, url_prefix='/ajax')


