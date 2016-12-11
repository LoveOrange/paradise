#!/usr/bin/python
# -*- coding:utf-8 -*-

from case_runner import CaseRunner


class DomCaseRunner(CaseRunner):

    def __init__(self, case):
        super(DomCaseRunner, self).__init__(case)

    def run(self):
        return self.case.validate
