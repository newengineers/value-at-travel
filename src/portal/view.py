from flask import Blueprint, url_for, render_template
from markupsafe import Markup


class View:

    path_base_view = 'base.html'
    path_view = 'views/%s/'
    path_skeleton_name = path_view+'_skeleton.html'

    def __init__(self, controller: Blueprint, view: str = 'index', args: any = None):
        self.controller = controller.name.lower()
        self.view = view
        self.arguments = args or {}

    def _append_resource(self, target_file: str, tmpl: str) -> str:
        path = self.path_view % self.controller
        path = url_for('static', filename=path+'_'+target_file)

        return tmpl % path

    def _render_controller(self) -> str:
        ctrl = self._append_resource('style.css', '<link rel="stylesheet" type="text/css" href="%s"/>')
        ctrl += render_template(self.path_skeleton_name % self.controller, **self.arguments)
        ctrl += self._append_resource('script.js', '<script src="%s"></script>')
        return ctrl

    def _render_view(self) -> str:
        view = self.path_view % self.controller+self.view+'.html'
        return render_template(view, **self.arguments)

    def render(self):
        self.arguments['view'] = Markup(self._render_view())
        self.arguments['controller'] = Markup(self._render_controller())

        return render_template(self.path_base_view, **self.arguments)

