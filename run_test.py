#!/usr/bin/python
#  -*- coding: utf-8 -*-

<<<<<<< HEAD
from src.case_handler import CaseHandler
from src.api_case_handler import ApiCaseHandler
from src.scripts_handler import ScriptsHandler
=======
from src.case_handler import *
from src.api_case_handler import *
from src.action_handler import *
>>>>>>> cf8b2dd254b3e95ae4f3655d7120b40a8bcd8fb8


def main():
    case_handler = CaseHandler()
    api_cases = case_handler.return_api_cases()
    base_config = case_handler.return_base_config()

<<<<<<< HEAD
    before_scripts = case_handler.return_before_scripts()
    before_scripts_handler = ScriptsHandler(before_scripts)
    before_scripts_handler.run()

=======
>>>>>>> cf8b2dd254b3e95ae4f3655d7120b40a8bcd8fb8
    api_case_handler = ApiCaseHandler(base_config["host"], api_cases)
    api_case_handler.run_test()

    action_handler = ActionHandler()


if __name__ == '__main__':
    main()
