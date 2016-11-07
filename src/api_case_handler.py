#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from api_case import ApiCase


class ApiCaseHandler(object):

    def __init__(self, host, cases):
        self.host = host
        self._case_data = cases
        self.api_cases = []

    def run_test(self):
        self._parse_cases()
        print 'start run api cases...'
        for case in self.api_cases:
            if 0 != case.test():
                sys.exit(-1)
        print 'all api ceses passed!\n'

    def _parse_cases(self):
        for case in self._case_data:
            for case_name in case.keys():
                api_case = ApiCase(self.host, case_name, case[case_name])
                self.api_cases.append(api_case)

