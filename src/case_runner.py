#!/usr/bin/python
# -*- coding:utf-8 -*-

from abc import abstractmethod
from action import Action
from expect import Expect
from expect_handler import validate

FAILED_CASES = []


def get_actions(case):
    _actions = []
    if "actions" not in case:
        return _actions
    for action in case["actions"]:
        _actions.append(Action(action))
    return _actions


class CaseRunner(object):
    """
    Abstract CaseRunner
    """

    def __init__(self, case):
        self.case = case
        self._actions = get_actions(self.case.case_body)
        self._run()

    def _run(self):
        print '- %s' % self.case.case_name
        self._run_actions()
        _validate = self.run()
        _expect = Expect(self.case.expect, _validate)
        if not validate(_expect):
            FAILED_CASES.append(self.case)

    def _run_actions(self):
        for action in self._actions:
            action.run()

    @abstractmethod
    def run(self):
        pass
