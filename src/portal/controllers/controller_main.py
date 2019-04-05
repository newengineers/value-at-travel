from flask import Blueprint
from flask_login import login_required

from portal.view import View
from portal.view_resource import ViewResource

main_controller = Blueprint('main', __name__)


@main_controller.route('/')
def index():
    return View(main_controller, view="index", resources={
        "index.css": ViewResource.StyleSheet
    }).render()


@main_controller.route('/map')
@login_required
def map():
    return View(main_controller, view="map", resources={
        "map.js": ViewResource.Script,
        "index.css": ViewResource.StyleSheet,
        "map.css": ViewResource.StyleSheet
    }).render()
