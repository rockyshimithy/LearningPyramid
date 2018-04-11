#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

api_endpoint = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'


def get_quotes():
    """
    Retrieve from API a dict with quotes

    :rtype: dict
    :return: A dictionary with all quotes
    """

    response = requests.get(api_endpoint)
    quotes = response.json()

    return quotes


def get_quote(quote_number):
    """
    Retrieve from API a string with a specify quote

    :param int quote_number: Identifier quote number
    :rtype: str
    :return: A string content with the specify quote
    """

    try:
        response = requests.get('{}/{}'.format(api_endpoint, quote_number))
        quote = response.json()['quote']
    except KeyError as error:
        raise KeyError('{} not found.'.format(error.args[0]))

    return quote
