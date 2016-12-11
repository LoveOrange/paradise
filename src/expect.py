#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml


class Expect(object):
    """
    Expect
    for extend
    """

    def __init__(self, expects, real):
        self.expects = expects
        self.real = real
