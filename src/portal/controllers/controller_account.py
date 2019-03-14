from flask import Blueprint
from portal.view import View

account_controller = Blueprint('account', __name__)
resources = {

}


@account_controller.route('/')
@account_controller.route('/login/')
def index():
    return View(account_controller).render()


@account_controller.route('/logout/')
def logout():
    return 'logout'


@account_controller.route('/register/')
def register():
    return 'register'
