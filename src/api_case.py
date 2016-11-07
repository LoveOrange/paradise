#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2

API = "api"
PARAMS = "params"
METHOD = "method"
EXPECT = "expect"

SUCCESS = 0
FAILURE = 1

EQUALS = "equals"


class ApiCase(object):
    """
    Api Case Class
    """
    def __init__(self, host, case_name, case_body):
        self.host = host
        self.name = case_name
        self.api = case_body[API]
        self.params = case_body[PARAMS]
        self.method = case_body[METHOD]
        self.expect = case_body[EXPECT]

    def test(self):
        print '* testing %s' % self.name
        if "get" == self.method:
            return self._test_get_request()
        return FAILURE

    def _test_get_request(self):
        url = self.host + self.api
        data = urllib.urlencode(self.params)
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        return self._parse_value(response.read())

    def _parse_value(self, real_value):
        for expect_mode in self.expect.keys():
            if EQUALS == expect_mode:
                if self.expect[EQUALS] == real_value:
                    return SUCCESS
                else:
                    print "...Error: expect %s but return %s" % (self.expect[EQUALS], real_value)
                    return FAILURE


