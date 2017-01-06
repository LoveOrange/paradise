#!/usr/bin/python
# -*- coding:utf-8 -*-

from action_handler import *


ACTION = {
    "click": click,
    "scripts": run_command,
    "fill": fill,
    "sleep": sleep
}


def _get_action(action):
    for k, v in action.items():
        return k, v


class Action(object):
    def __init__(self, action, url):
        self._action_type, self._action_value = _get_action(action)
        self.url = url

    def run(self):
        ACTION[self._action_type](self._action_value)
