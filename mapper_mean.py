#!/usr/bin/env python3

import sys

def read_input(src=sys.stdin, separator=","):
	try:
		line = src.read()
		line_splitted = line.split(separator)
		yield line_splitted
	except Exception as e:
		raise(e)

def main():
	try:
		data = read_input()
		for d in data:
			print(d[8])
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()