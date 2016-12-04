#!/usr/bin/python
# -*- coding:utf-8 -*-

from command_handler import Command


def click(dom):
    """
    click specific dom
    :param dom:
    :return:
    """
    print "click " + dom


def run_command(_command):
    """
    run shell command
    :param _command:
    :return:
    """
    command = Command(_command)
    command.run()


ACTION = {
    "click": click,
    "scripts": run_command
}


def get_action(action):
    for k, v in action.items():
        return k, v


class Action(object):

    def __init__(self, action):
        self._action_type, self._action_value = get_action(action)

    def run(self):
        ACTION[self._action_type](self._action_value)
