#!/usr/bin/python
# -*- coding:utf-8 -*-


class Case(object):
    """
    Case抽象类
    """

    def __init__(self, _type, case):
        self.type = _type
        for k in case.keys():
            self.case_name = k
            self.case_body = case[k]
            break
