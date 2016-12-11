#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium import webdriver


class SeleniumUtils(object):

    def __init__(self):
        print "init"
        self._browser = webdriver.Chrome()

    def check_title(self, expect):
        self._browser.get("https://github.com")
        return expect == self._browser.title

    def click(self, dom):
        self._browser.get("https://baidu.com")

    def fill(self, dom, value):
        _dom = self._browser.find_element_by_class_name(dom)
        _dom.send_keys(value)
        print 'I love chengzi'


browser = None


def get_browser():
    global browser
    if browser is None:
        browser = SeleniumUtils()
    return browser
