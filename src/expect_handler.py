#!/usr/bin/python
# -*- coding:utf-8 -*-


def _equals(expect, real):
    return expect == real


def _pass(expect, real):
    return True


def _status_code(expect, real):
    return expect == real.status_code


EXPECT = {
    "equals": _equals,
    "pass": _pass,
    "status_code": _status_code
}


def validate(expect):
    _validate = True
    real = expect.real
    # print expect.real
    for case in expect.expects:
        for k, v in case.items():
            _validate &= EXPECT[k](v, real)
    return _validate
