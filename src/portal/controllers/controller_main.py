from flask import Blueprint

from portal.view import View

main_controller = Blueprint('main', __name__)


@main_controller.route('/')
def index():

    args = {
        'test': 'Hello World'
    }

    return View(main_controller, args=args).render()
