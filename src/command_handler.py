#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import subprocess


class Command(object):

    def __init__(self, command):
        self.command = command

    def run(self):
        process = subprocess.Popen(self.command, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not 0 == process.wait():
            print('Error with current command: [%s]' % self.command)
            sys.exit(-1)
