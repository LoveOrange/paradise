#!/usr/bin/python
# -*- coding:utf-8 -*-


def _equals(expect, real):
    return expect == real


def _pass(expect, real):
    return True


EXPECT = {
    "equals": _equals,
    "pass": _pass
}


def validate(expect):
    _validate = True
    real = expect.real
    # print expect.real
    for case in expect.expects:
        for k, v in case.items():
            _validate &= EXPECT[k](v, real)
    return _validate
