# https://www.football-data.org/documentation/api
# API GUIDE https://www.football-data.org/documentation/quickstart

# must set environment variable  called SSC_KEY with your api key in .bashrc or .zshrc
# eg. export SSC_KEY = "YourKeyHere"

import term_output  # local term_output.py
import dictionaries as config
import sys
from termcolor import colored


print("Pick a code from the following: ")
term_output.print_teams()

entry = input(": ")

# term_output.test_standings(config.codes[entry])
#print(term_output.test())

term_output.get_standings(entry)

# hi = "hi"
# hi = colored(hi, "cyan")
# hi = colored(hi, attrs=["bold"])
# print(hi)