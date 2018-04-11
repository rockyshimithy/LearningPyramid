#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from backends.api_quote import get_quote, get_quotes

def test_get_quotes_with_success():
    quotes = get_quotes()

    dict_quotes = { "quotes": [ "Beautiful is better than ugly.",
                                "Explicit is better than implicit.",
                                "Simple is better than complex.",
                                "Complex is better than complicated.",
                                "Flat is better than nested.",
                                "Sparse is better than dense.",
                                "Readability counts.",
                                "Special cases aren't special enough to break the rules.",
                                "Although practicality beats purity.",
                                "Errors should never pass silently.",
                                "Unless explicitly silenced.",
                                "In the face of ambiguity, refuse the temptation to guess.",
                                "There should be one-- and preferably only one --obvious way to do it.",
                                "Although that way may not be obvious at first unless you're Dutch.",
                                "Now is better than never.",
                                "Although never is often better than *right* now.",
                                "If the implementation is hard to explain, it's a bad idea.",
                                "If the implementation is easy to explain, it may be a good idea.",
                                "Namespaces are one honking great idea -- let's do more of those!"]
                    }

    assert quotes == dict_quotes


def test_get_quote_with_success():
    quote = get_quote(3)

    assert quote == "Complex is better than complicated."


def test_get_quote_not_found():
    with pytest.raises(KeyError) as excption_info:
        get_quote(30)

    assert excption_info.value.args[0] == 'quote not found.'