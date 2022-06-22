#!/usr/bin/env python3

import sys

try:
	for line in sys.stdin:
		data = line.split(",")
		print('{0}\t{1}'.format(data[3], 1))
except Exception as e:
	raise(e)