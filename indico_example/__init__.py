from flask_pluginengine import render_plugin_template, current_plugin, with_plugin_context
from wtforms import StringField, BooleanField

from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint
from indico.modules.rb.forms.base import IndicoForm
from MaKaC.webinterface.rh.base import RH
from MaKaC.webinterface.pages.main import WPMainBase


class SettingsForm(IndicoForm):
    dummy_message = StringField('Dummy Message')
    show_message = BooleanField('Show Message')


class ExamplePlugin(IndicoPlugin):
    """Example Plugin

    An example plugin that demonstrates the capabilities of the new Indico plugin system.
    """

    settings_form = SettingsForm

    def init(self):
        super(ExamplePlugin, self).init()
        self.inject_css('global_css')
        self.inject_js('global_js')

    def get_blueprints(self):
        return blueprint

    def add_cli_command(self, manager):
        @manager.command
        @with_plugin_context(self)
        def example():
            """Example command from example plugin"""
            print 'example plugin says hi', current_plugin
            if self.settings.get('show_message'):
                print self.settings.get('dummy_message')

    def extend_shell_context(self, add_to_context):
        add_to_context('bar', name='foo', doc='foobar from example plugin', color='magenta!')

    def register_assets(self):
        self.register_js_bundle('example_js', 'js/example.js')
        self.register_js_bundle('global_js', 'js/global.js')
        self.register_css_bundle('example_css', 'css/example.scss')
        self.register_css_bundle('global_css', 'css/global.scss')


blueprint = IndicoPluginBlueprint('example', __name__)


class WPExample(WPMainBase):
    def _getBody(self, params):
        return render_plugin_template('example.html', **params)


class RHExample(RH):
    def _process(self):
        return WPExample(self, foo=u'bar').display()


class RHTest(RH):
    def _process(self):
        return render_plugin_template('test.html')


blueprint.add_url_rule('/example', 'example', view_func=RHExample)
blueprint.add_url_rule('/example/x', 'example', view_func=RHExample)
blueprint.add_url_rule('/test', 'test', view_func=RHTest)
