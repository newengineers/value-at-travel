from flask import Flask, redirect, url_for
from flask_login import LoginManager

from portal.controllers.controller_ajax import ajax_controller
from system.models.user import User
from .controllers.controller_account import account_controller
from .controllers.controller_api import api_controller
from .controllers.controller_main import main_controller

app = Flask(__name__,
            static_url_path='/frontend',
            static_folder='frontend',
            template_folder='frontend')
app.secret_key = 'da39a3ee5e6b4b0d3255beef95601890afd80709'
app_login = LoginManager()
app_login.init_app(app)


@app_login.user_loader
def load_user(id_ref: int) -> User:
    from system.database import Database
    session = Database.get_instance().get_session()
    return session.query(User).filter_by(id=id_ref).first()


@app_login.unauthorized_handler
def unauthorized():
    return redirect(url_for('account.index'))


app.register_blueprint(main_controller, url_prefix='/')
app.register_blueprint(account_controller, url_prefix='/account')
app.register_blueprint(api_controller, url_prefix='/api')
app.register_blueprint(ajax_controller, url_prefix='/ajax')