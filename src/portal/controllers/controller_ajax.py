from flask import Blueprint

from portal.resource import Resource

ajax_controller = Blueprint('ajax', __name__)

@ajax_controller.route('/request-login', methods=['POST'])
def request_login():