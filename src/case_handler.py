#!/usr/bin/python
#  -*- coding: utf-8 -*-

from api_case_handler import ApiCaseHandler
from dom_case_handler import DomCaseHandler


def case_log_start():
    print "start loading cases..."


def case_log_end():
    print "loading cases complete.\n"


class CaseHandler(object):
    """
    Case Handler
    read cases from *.yml
    """
    def __init__(self, config):
        self.config = config
        self._cases = []

    def load_cases(self):
        case_log_start()
        for case_file in self.config.case_files:
            # todo 优化
            if "api" in case_file:
                self._cases.extend(ApiCaseHandler(case_file["api"], self.config).load_cases())
            elif "dom" in case_file:
                self._cases.extend(DomCaseHandler(case_file["dom"], self.config).load_cases())
        case_log_end()
        return self._cases
