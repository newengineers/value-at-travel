from flask import Blueprint

from portal.authentication import auth_required
from portal.resource import Resource
from portal.view import View

main_controller = Blueprint('main', __name__)


@main_controller.route('/')
def index():
    return View(main_controller, view="index", resources={
        "index.css": Resource.StyleSheet
    }).render()


@main_controller.route('/map')
@auth_required
def map():
    return View(main_controller, view="map", resources={
        "map.js": Resource.Script,
        "map.css": Resource.StyleSheet
    }).render()

