from flask import Flask

from .controllers.controller_account import account_controller
from .controllers.controller_api import api_controller
from .controllers.controller_main import main_controller

app = Flask(__name__,
            static_url_path='/frontend',
            static_folder='frontend',
            template_folder='frontend')

app.register_blueprint(main_controller, url_prefix='/')
app.register_blueprint(account_controller, url_prefix='/account')
app.register_blueprint(api_controller, url_prefix='/api')


