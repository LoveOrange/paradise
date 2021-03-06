#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from .case_runner import FAILED_CASES
from .runner_factory import RUNNER_FACTORY

CONFIG_FILE = "config.yml"


def start_test_log():
    print("start testing...\n")


def end_test_log():
    print("\ntesting complete\n")
    if len(FAILED_CASES) > 0:
        print("some cases are failed:")
        for case in FAILED_CASES:
            print("- %s" % case.case_name)
        sys.exit(-1)
    else:
        print("all cases passed")


def start_test(cases):
    start_test_log()
    for case in cases:
        RUNNER_FACTORY[case.type](case)
    end_test_log()
