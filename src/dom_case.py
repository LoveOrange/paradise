#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
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
        super(DomCase, self).__init__("dom", case)
        self._actions = get_actions(self.case_body)
        self._validate = get_validate(self.case_body)
        self._expect = get_expect(self.case_body)
        self.check_dom_correct()

    def check_dom_correct(self):
        if not self._validate:
            print "[Error] None validate dom, return -1"
            sys.exit(-1)
