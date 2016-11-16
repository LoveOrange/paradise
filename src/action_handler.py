#!/usr/bin/python
# -*- coding:utf-8 -*-


class ActionHandler(object):

    def __init__(self, action_config):
        self._action_config = action_config

    def run_before(self):
        before_action = self._parse_before_action()
        if before_action:
            if "scripts" in before_action:
                pass

    def _parse_before_action(self):
        if "before" in self._action_config:
            return self._action_config["before"]
        return None
