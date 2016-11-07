#!/usr/bin/python
#  -*- coding: utf-8 -*-

import yaml

BASE = "base"
CASES_PATH = "cases/main.yml"
API_TEST = "api_test"


class CaseHandler(object):
    """
    Case Handler
    read cases from .yml
    """
    def __init__(self):
        self._case_yml_path = CASES_PATH
        self._all_config = {}

        self._read_yml()

    def _read_yml(self):
        with open(self._case_yml_path, 'r') as cases_yml:
            self._all_config = yaml.load(cases_yml)

    def return_base_config(self):
        return self._all_config[BASE]

    def return_api_cases(self):
        if API_TEST in self._all_config:
            return self._all_config[API_TEST]


