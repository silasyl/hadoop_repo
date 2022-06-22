#!/usr/bin/env python3

import sys

curr_key = None
curr_count = 0

try:
	for line in sys.stdin:
		key, count = line.split("\t", 1)
		count = int(count)
		if key == curr_key:
			curr_count += count
		else:
			if curr_key:
				print('{0}\t{1}'.format(curr_key, curr_count))
			curr_count = count
			curr_key = key
	if curr_key == key:
		print('{0}\t{1}'.format(curr_key, curr_count))
except Exception as e:
	raise(e)