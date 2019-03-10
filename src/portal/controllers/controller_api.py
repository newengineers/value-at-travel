from flask import Blueprint

api_controller = Blueprint('api', __name__)


@api_controller.route('/')
def index():
    return 'api not found'
