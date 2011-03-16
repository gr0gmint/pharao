from pyramid.config import Configurator
from pharao.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('pharao.views.my_view',
                    context='pharao:resources.Root',
                    renderer='pharao:templates/mytemplate.pt')
    config.add_static_view('static', 'pharao:static')
    config.scan()
    config.scan('pharao:model')
    config.scan('pharao:views')
    return config.make_wsgi_app()

