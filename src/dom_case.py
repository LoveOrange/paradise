#!/usr/bin/python
# -*- coding:utf-8 -*-

from case import Case
from action import Action


def get_actions(case):
    _actions = []
    if "actions" not in case:
        return _actions
    for action in case["actions"]:
        _actions.append(Action(action))
    return _actions


def get_validate(case):
    if "validate" in case:
        return case["validate"]


def get_expect(case):
    return case


class DomCase(Case):
    """
    Dom Case
    """

    def __init__(self, case):
        super(DomCase, self).__init__("DOM", case)
        self._actions = get_actions(case)
        self._validate = get_validate(case)
        self._expect = get_expect(case)
