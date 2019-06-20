#!/usr/bin/python
# -*- coding:utf-8 -*-

from .case_runner import CaseRunner
from .selenium_utils import get_browser


class DomCaseRunner(CaseRunner):

    def __init__(self, case):
        super(DomCaseRunner, self).__init__(case)

    def run(self):
        if "title" == self.case.validate:
            return get_browser(self.case.case_body["url"]).get_title()
        else:
            return get_browser(self.case.case_body["url"]).get(self.case.validate)
