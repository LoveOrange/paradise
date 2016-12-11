#!/usr/bin/python
# -*- coding:utf-8 -*-


def _equals(expect, real):
    return expect == real


EXPECT = {
    "equals": _equals
}


def validate(expect):
    _validate = True
    real = expect.real
    for case in expect.expects:
        for k, v in case.items():
            _validate &= EXPECT[k](v, real)
    return _validate
