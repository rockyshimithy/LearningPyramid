#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from backends.api_quote import get_quotes, get_quote

from pyramid.view import view_config, view_defaults
from pyramid.response import Response


@view_defaults(renderer='templates/quote.jinja2')
class QuoteViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='index')
    def index(self):
        return {}

    @view_config(route_name='quotes')
    def quotes(self):
        quotes = get_quotes()
        return {'quotes': quotes['quotes']}

    @view_config(route_name='quote')
    def quote(self):
        quote = []
        quote_id = self.request.matchdict['quote_id']
        quote.append(get_quote(quote_id))
        return {'quotes': quote}

    @view_config(route_name='random_quote')
    def random_quote(self):
        quote = []
        quotes = get_quotes()
        quote.append(random.choice(quotes['quotes']))
        index = quotes['quotes'].index(quote[0])
        return {'quotes': quote, 'index': index}


@view_config(route_name='sessions')
def sessions(request):
    import ipdb; ipdb.set_trace()
    return Response('Sessions')