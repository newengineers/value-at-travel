from flask import Blueprint, request

from portal.authentication import AuthSession

ajax_controller = Blueprint('ajax', __name__)


@ajax_controller.route('/request-login/', methods=['GET', 'POST'])
def request_login():
    auth_session = AuthSession()
    auth_session.construct(1)
    username = request.form.get('user')
    print("Username: ", username)

    return '200'
