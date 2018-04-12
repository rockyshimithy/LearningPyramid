from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    #config.add_static_view('static', 'static', cache_max_age=3600) # TODO: WHAT THIS MEANS ?

    config.add_route('index', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('random_quote', '/quotes/random')
    config.add_route('quote', '/quotes/{quote_id}')

    config.scan('.views')

    return config.make_wsgi_app()
