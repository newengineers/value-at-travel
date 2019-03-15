from flask import Blueprint

from portal.authentication import auth_required
from portal.resource import Resource
from portal.view import View

main_controller = Blueprint('main', __name__)
resources = {
    "map.js":   Resource.Script,
    "map.css":  Resource.StyleSheet
}


@main_controller.route('/')
@auth_required
def index():
    return View(main_controller, resources=resources).render()
