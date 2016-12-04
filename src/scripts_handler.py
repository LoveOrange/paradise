#!/usr/bin/python
# -*- coding:utf-8 -*-

from script_action import ScriptAction


class ScriptsHandler(object):

    def __init__(self, scripts):
        self.scripts = scripts

    def run(self):
        for _script in self.scripts:
            script = ScriptAction(_script)
            script.run()
