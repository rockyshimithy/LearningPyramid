#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import uuid

from backends.api_quote import get_quotes, get_quote
from api_pyramid_quote.models import DBSession, Session

from pyramid.view import view_config, view_defaults
from pyramid.response import Response


@view_defaults(renderer='templates/quote.jinja2')
class QuoteViews:
    def __init__(self, request):
        self.request = request
        self.session = verify_uuid_session(request.session)

    @view_config(route_name='index')
    def index(self):
        add_session(self.session['uuid'], self.request.route_path('index'))
        return {}

    @view_config(route_name='quotes')
    def quotes(self):
        add_session(self.session['uuid'], self.request.route_path('quotes'))

        quotes = get_quotes()
        return {'quotes': quotes['quotes']}

    @view_config(route_name='quote')
    def quote(self):
        quote_id = self.request.matchdict['quote_id']
        add_session(self.session['uuid'], self.request.route_path('quote', quote_id=quote_id))

        quote = []
        try:
            quote.append(get_quote(quote_id))
        except KeyError:
            return Response('Quote {} not Found.'.format(quote_id))

        return {'quotes': quote}

    @view_config(route_name='random_quote')
    def random_quote(self):
        add_session(self.session['uuid'], self.request.route_path('random_quote'))

        quote = []
        quotes = get_quotes()
        quote.append(random.choice(quotes['quotes']))
        index = quotes['quotes'].index(quote[0])
        return {'quotes': quote, 'index': index}


@view_config(route_name='sessions', renderer='templates/sessions.jinja2')
def view_sessions(request):
    session = request.session
    session = verify_uuid_session(session)

    add_session(session['uuid'], request.route_path('sessions'))

    sessions = DBSession.query(Session).all()

    return {'sessions': sessions}


def verify_uuid_session(session):
    if 'uuid' not in session:
        session['uuid'] = uuid.uuid4().hex

    return session


def add_session(uuid_session, route_name):
    session = Session(uuid_session=uuid_session, route_name=route_name)
    DBSession.add(session)
