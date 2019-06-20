#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from .case import Case


def get_validate(case):
    if "validate" in case:
        return case["validate"]


class DomCase(Case):
    """
    Dom Case
    """

    def __init__(self, case):
        super(DomCase, self).__init__("dom", case)
        self.validate = get_validate(self.case_body)
        self.check_dom_correct()

    def check_dom_correct(self):
        pass
        # if not self.validate:
        #     print "[Error] None validate dom, return -1"
        #     sys.exit(-1)
