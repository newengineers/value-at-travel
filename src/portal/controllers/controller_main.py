from flask import Blueprint

from portal.view import View

main_controller = Blueprint('main', __name__)
resources = {}


@main_controller.route('/')
def index():
    return View(main_controller, resources=resources).render()
