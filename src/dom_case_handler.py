#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml
import sys
from .dom_case import DomCase


class DomCaseHandler(object):

    def __init__(self, case_file, config):
        self._api_cases = []
        self._case_file = case_file
        self._config = config

    def load_cases(self):
        # todo 代码重复，优化
        try:
            with open(self._case_file) as _case_file:
                case_files = yaml.safe_load(_case_file)
        except IOError:
            print("[Error] case file not exists: %s" % self._case_file)
            sys.exit(-1)
        for case in case_files:
            self._api_cases.append(DomCase(case))
        return self._api_cases
