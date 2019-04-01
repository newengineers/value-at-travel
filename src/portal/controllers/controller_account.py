from flask import Blueprint, redirect, url_for
from flask_login import logout_user, current_user, login_required

from portal.view import View
from portal.view_resource import ViewResource

account_controller = Blueprint('account', __name__)
resources = {
    'login.css': ViewResource.StyleSheet,
    'login.js': ViewResource.Script
}


@account_controller.route('/')
@account_controller.route('/login/')
@account_controller.route('/register/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    return View(account_controller, resources=resources).render()


@account_controller.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('account.index'))
