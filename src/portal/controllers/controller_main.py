from flask import Blueprint

from portal.resource import Resource
from portal.view import View

main_controller = Blueprint('main', __name__)
resources = {
    'temp.js': Resource.Script
}


@main_controller.route('/')
def index():
    return View(main_controller, resources=resources).render()
