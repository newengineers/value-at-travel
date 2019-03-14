from flask import Blueprint

from portal.resource import Resource
from portal.view import View

main_controller = Blueprint('main', __name__)
resources = {
    "map.js":   Resource.Script,
    "map.css":  Resource.StyleSheet
}


@main_controller.route('/')
def index():
    return View(main_controller, resources=resources).render()
