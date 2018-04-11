#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

api_endpoint = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'


# Consulta API e retorna dicionário python contendo os quotes
# TODO: Fix comments to be Docstring
def get_quotes():
    response = requests.get(api_endpoint)
    quotes = response.json()

    return quotes

# Consulta API e retorna o quote correspondente
# TODO: Fix comments to be Docstring
def get_quote(quote_number):
    try:
        response = requests.get('{}/{}'.format(api_endpoint, quote_number))
        quote = response.json()['quote']
    except KeyError as error:
        raise KeyError('{} not found.'.format(error.args[0]))

    return quote
