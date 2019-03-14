from flask import Blueprint, url_for, render_template
from markupsafe import Markup

from portal.resource import Resource


stylesheets = [
    'normalize',
    # 'bootstrap.min',
    # 'bootstrap-theme.min',
    'main'
]

scripts = [
    'jquery.min',
    # 'bootstrap.min',
    'main'
]


class View:

    path_base_view = 'base.html'
    path_view = 'views/%s/'
    path_skeleton_name = path_view+'_skeleton.html'
    path_resources_folder = path_view+'resources/'

    def __init__(self, controller: Blueprint,
                 view: str = 'index',
                 args: any = None,
                 resources: dict = None):
        self.controller = controller.name.lower()
        self.view = view
        self.arguments = args or {}
        self.resources = resources or {}

    def _construct_resources(self, resource: Resource, template: str) -> str:
        markup = ''
        for key, value in self.resources.items():
            if isinstance(value, Resource) and value is resource:
                path = self.path_resources_folder % self.controller
                path = url_for('static', filename=path+key)

                markup += template % path

        return markup

    def _construct_controller(self) -> str:
        ctrl = self._construct_resources(Resource.StyleSheet, '<link rel="stylesheet" type="text/css" href="%s"/>')
        ctrl += render_template(self.path_skeleton_name % self.controller, **self.arguments)
        ctrl += self._construct_resources(Resource.Script, '<script src="%s"></script>')

        return ctrl

    def _construct_view(self) -> str:
        view = self.path_view % self.controller+self.view+'.html'
        return render_template(view, **self.arguments)

    def render(self):
        self.arguments['view'] = Markup(self._construct_view())
        self.arguments['controller'] = Markup(self._construct_controller())
        self.arguments['global_scripts'] = scripts
        self.arguments['global_styling'] = stylesheets

        return render_template(self.path_base_view, **self.arguments)
