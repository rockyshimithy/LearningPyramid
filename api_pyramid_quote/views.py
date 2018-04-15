#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import uuid

from backends.api_quote import get_quotes, get_quote
from api_pyramid_quote.models import DBSession, Session

from pyramid.view import view_config, view_defaults


@view_defaults(renderer='templates/quote.jinja2')
class QuoteViews:
    def __init__(self, request):
        self.request = request
        self.session = request.session

    @view_config(route_name='index')
    def index(self):

        # TODO : CREATE DECORATOR OR FUNCTION
        if 'uuid' not in self.session:
            self.session['uuid'] = uuid.uuid4().hex

        session = Session(uuid_session=self.session['uuid'], route_name=self.request.route_path('index'))
        DBSession.add(session)

        return {}

    @view_config(route_name='quotes')
    def quotes(self):

        if 'uuid' not in self.session:
            self.session['uuid'] = uuid.uuid4().hex

        session = Session(uuid_session=self.session['uuid'], route_name=self.request.route_path('quotes'))
        DBSession.add(session)

        quotes = get_quotes()
        return {'quotes': quotes['quotes']}

    @view_config(route_name='quote')
    def quote(self):
        quote_id = self.request.matchdict['quote_id']

        if 'uuid' not in self.session:
            self.session['uuid'] = uuid.uuid4().hex

        session = Session(uuid_session=self.session['uuid'],
                          route_name=self.request.route_path('quote', quote_id=quote_id))
        DBSession.add(session)

        quote = []
        quote.append(get_quote(quote_id))
        return {'quotes': quote}

    @view_config(route_name='random_quote')
    def random_quote(self):

        if 'uuid' not in self.session:
            self.session['uuid'] = uuid.uuid4().hex

        session = Session(uuid_session=self.session['uuid'], route_name=self.request.route_path('random_quote'))
        DBSession.add(session)

        quote = []
        quotes = get_quotes()
        quote.append(random.choice(quotes['quotes']))
        index = quotes['quotes'].index(quote[0])
        return {'quotes': quote, 'index': index}


@view_config(route_name='sessions', renderer='templates/sessions.jinja2')
def sessions(request):
    session = request.session
    if 'uuid' not in session:
        session['uuid'] = uuid.uuid4().hex

    session = Session(uuid_session=session['uuid'], route_name=request.route_path('sessions'))
    DBSession.add(session)

    sessions = DBSession.query(Session).all()

    return {'sessions': sessions}
