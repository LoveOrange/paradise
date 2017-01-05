#!/usr/bin/python
# -*- coding:utf-8 -*-


def get_type(value):
    if value.startswith("."):
        return "class"
    elif value.startswith("#"):
        return "id"
    else:
        return "div"


def get_dom(value):
    if value.startswith(".") or value.startswith("#"):
        value = value[1:]
    if "(" in value:
        return value[:value.index("(")]
    else:
        return value


def get_params(value):
    if "(" in value:
        return value[value.index("(") + 1:-1]
    return ""


class Dom:
    """
    Dom obj, for dom dsl
    """
    def __init__(self, value):
        self.value = value
        self.type = get_type(value)
        self.dom = get_dom(value)
        self.params = get_params(value)
