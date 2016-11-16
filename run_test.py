#!/usr/bin/python
#  -*- coding: utf-8 -*-

from src.case_handler import CaseHandler
from src.api_case_handler import ApiCaseHandler
from src.scripts_handler import ScriptsHandler


def main():
    case_handler = CaseHandler()
    api_cases = case_handler.return_api_cases()
    base_config = case_handler.return_base_config()

    before_scripts = case_handler.return_before_scripts()
    before_scripts_handler = ScriptsHandler(before_scripts)
    before_scripts_handler.run()

    api_case_handler = ApiCaseHandler(base_config["host"], api_cases)
    api_case_handler.run_test()


if __name__ == '__main__':
    main()
