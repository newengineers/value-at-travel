from flask import Blueprint

from portal.resource import Resource
from portal.view import View

account_controller = Blueprint('account', __name__)
resources = {
    'style.css': Resource.StyleSheet,
    'forms.js': Resource.Script
}


@account_controller.route('/')
@account_controller.route('/login/')
def index():
    return View(account_controller, resources=resources).render()


@account_controller.route('/logout/')
def logout():
    return 'logout'


@account_controller.route('/register/')
def register():
    return 'register'
