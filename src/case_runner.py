#!/usr/bin/python
# -*- coding:utf-8 -*-
from abc import abstractmethod


class CaseRunner(object):
    """
    Abstract CaseRunner
    """

    def __init__(self, cases):
        self.cases = cases

    @abstractmethod
    def run(self):
        pass
