#!/usr/bin/env python3

import re

regex = '^((:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]).{0,1}){4}$'
print(re.fullmatch(regex, '12.128.54.200', flags=0))
