#!/usr/bin/python
# -*- coding:utf-8 -*-

from src.runner_factory import RUNNER_FACTORY

CONFIG_FILE = "config.yml"


def start_test_log():
    print "start testing..."


def end_test_log():
    print "testing complete"


def start_test(cases):
    start_test_log()
    for case in cases:
        RUNNER_FACTORY[case.type](case)
    end_test_log()
