#!/usr/bin/python
# -*- coding:utf-8 -*-

from .command_handler import Command

SUCCESS = 0
FAILURE = 1


class ScriptAction(object):

    def __init__(self, command):
        self.command = command

    def run(self):
        command = Command(self.command)
        return command.run()
