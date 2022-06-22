#!/usr/bin/env python3

import sys

def read_input(src=sys.stdin, separator='\n'):
	try:
		line = src.read().strip()
		line_splitted = line.split(separator)

		for item in line_splitted:
			yield item
	except Exception as e:
		raise(e)

def main():
	count = 0
	sum = 0
	try:
		data = read_input()
		for d in data:
			sum += float(d)
			count += 1

		print(f"Average: {sum/count}")
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()