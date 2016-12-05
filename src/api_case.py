#!/usr/bin/python
# -*- coding:utf-8 -*-

from case import Case


class ApiCase(Case):
    """
    Api Case Class
    """

    def __init__(self, case):
        # todo api test功能与 pyresttest 相似，暂时先做dom
        super(ApiCase, self).__init__("api", case)
        pass
