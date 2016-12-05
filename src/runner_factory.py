#!/usr/bin/python
# -*- coding:utf-8 -*-

from api_case_runner import ApiCaseRunner
from dom_case_runner import DomCaseRunner

_API_CASE_RUNNER = ApiCaseRunner
_DOM_CASE_RUNNER = DomCaseRunner

RUNNER_FACTORY = {
    "api": _API_CASE_RUNNER,
    "dom": _DOM_CASE_RUNNER
}
