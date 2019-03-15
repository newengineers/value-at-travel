from flask import Blueprint
from portal.authentication import AuthSession

ajax_controller = Blueprint('ajax', __name__)


@ajax_controller.route('/request-login/', methods=['GET', 'POST'])
def request_login():
    auth_session = AuthSession()
    auth_session.construct(1)

    return 'Connection OK'
