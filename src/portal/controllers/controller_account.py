from flask import Blueprint

account_controller = Blueprint('account', __name__)


@account_controller.route('/')
@account_controller.route('/login/')
def index():
    return 'account'


@account_controller.route('/logout/')
def logout():
    return 'login'


@account_controller.route('/register/')
def register():
    return 'register'
