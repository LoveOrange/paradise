#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from .case_runner import CaseRunner


class ApiCaseRunner(CaseRunner):

    def __init__(self, case):
        super(ApiCaseRunner, self).__init__(case)

    def run(self):
        response = None
        url = self.case.case_body["url"]
        headers = self.case.case_body["headers"]
        params = self.case.case_body["params"]
        if self.case.case_body["method"] == "get":
            response = requests.get(url=url, data=params, headers=headers)
        elif self.case.case_body["method"] == "post":
            response = requests.post(url=url, data=params, headers=headers)
        elif self.case.case_body["method"] == "put":
            response = requests.put(url=url, data=params, headers=headers)
        return response
