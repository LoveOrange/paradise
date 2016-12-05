#!/usr/bin/python
# -*- coding:utf-8 -*-
from abc import abstractmethod


class CaseRunner(object):
    """
    Abstract CaseRunner
    """

    def __init__(self, case):
        self.case = case

    @abstractmethod
    def run(self):
        pass
