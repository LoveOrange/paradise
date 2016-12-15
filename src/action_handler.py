#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
from command_handler import Command
from selenium_utils import get_browser


def click(dom):
    """
    click specific dom
    :param dom:
    :return:
    """
    get_browser().click(dom)


def run_command(_command):
    """
    run shell command
    :param _command:
    :return:
    """
    command = Command(_command)
    command.run()


def fill(dom):
    get_browser().fill("s_ipt")
    pass


def sleep(timeout):
    time.sleep(timeout)
