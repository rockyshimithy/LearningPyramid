#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Session(Base):
    __tablename__ = 'session'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    uuid_session = Column('uuid_session', Text)
    route_name = Column('route_name', Text)
    datetime = Column('datetime', DateTime, default=datetime.datetime.now)
