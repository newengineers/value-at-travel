from flask import Blueprint

from portal.view import View
from portal.view_resource import ViewResource

main_controller = Blueprint('main', __name__)


@main_controller.route('/')
def index():
    return View(main_controller, view="index", resources={
        "index.css": ViewResource.StyleSheet
    }).render()


@main_controller.route('/map')
def map():
    return View(main_controller, view="map", resources={
        "map.js": ViewResource.Script,
        "map.css": ViewResource.StyleSheet
    }).render()
