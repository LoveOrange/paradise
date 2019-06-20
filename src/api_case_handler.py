#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import yaml
from .api_case import ApiCase


class ApiCaseHandler(object):

    def __init__(self, case_file, config):
        self._api_cases = []
        self._case_file = case_file
        self._config = config

    def load_cases(self):
        try:
            with open(self._case_file) as _case_file:
                case_files = yaml.load(_case_file, Loader=yaml.CLoader)
        except IOError:
            print("[Error] case file not exists: %s" % self._case_file)
            sys.exit(-1)
        for case in case_files:
            self._api_cases.append(ApiCase(case))
        return self._api_cases
