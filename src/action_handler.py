#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
from command_handler import Command
from selenium_utils import get_browser


url = None


def init(case_url):
    global url
    url = case_url


def click(dom):
    """
    click specific dom
    :param dom:
    :return:
    """
    get_browser(url).click(dom)


def run_command(_command):
    """
    run shell command
    :param _command:
    :return:
    """
    command = Command(_command)
    command.run()


def fill(dom):
    get_browser(url).fill(dom)
    pass


def sleep(timeout):
    time.sleep(timeout)
