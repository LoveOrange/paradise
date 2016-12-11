#!/usr/bin/python
# -*- coding:utf-8 -*-

from case_runner import CaseRunner


class ApiCaseRunner(CaseRunner):

    def __init__(self, case):
        super(ApiCaseRunner, self).__init__(case)

    def run(self):
        return "ok"
