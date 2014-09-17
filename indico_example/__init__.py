from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint
from indico.web.flask.util import url_for

# TODO: assets
# TODO: database


class ExamplePlugin(IndicoPlugin):
    def init(self):
        signals.cli.connect(self.add_cli_command)
        signals.shell_context.connect(self.extend_shell_context)
        signals.get_blueprints.connect(self.get_blueprints)

    def add_cli_command(self, manager):
        @manager.command
        def example():
            """Example command from example plugin"""
            print 'example plugin says hi'

    def extend_shell_context(self, sender, add_to_context):
        add_to_context('bar', name='foo', doc='foobar from example plugin', color='magenta!')

    def get_blueprints(self, app):
        return blueprint


blueprint = IndicoPluginBlueprint('example', __name__)


@blueprint.route('/example')
def example():
    return 'example blueprint says hi<br>' \
           '<a href="{0}">{0}</a>'.format(url_for('example.static', filename='images/cat.jpg'))
