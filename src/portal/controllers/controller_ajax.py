from flask import Blueprint, request

from system.database_queries.orm_query import UserInfo
from portal.authentication import AuthSession

ajax_controller = Blueprint('ajax', __name__)


@ajax_controller.route('/request-login/', methods=['GET', 'POST'])
def request_login():
    auth_session = AuthSession()
    user = request.args.get("user")
    password = request.args.get("password")
    user_data = UserInfo.get_user_info("test")
    for users in user_data:
        if user == users.username and users.password == password:
            LOGGED_IN = True
            return '200'
        else:
            return 'error'

