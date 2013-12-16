#!/usr/bin/env python
# encoding: utf-8
"""
b.py

https://code.google.com/codejam/contest/2437488/dashboard#s=a&a=1

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	source = open('b.in', 'r')
	for T in range(int(source.readline())):
		x, y = map(int, source.readline().split())

		N = 0
		total = 0
		while total < abs(x) + abs(y) or (total + x + y) % 2 == 1:
			N += 1
			total += N
		
		result = ""
		while N > 0:
			if abs(x) > abs(y):
				if x > 0:
					result += 'E'
					x -= N
				else:
					result += 'W'
					x += N
			else:
				if y > 0:
					result += 'N'
					y -= N
				else:
					result += 'S'
					y += N
			N -= 1

		print "Case #%d: %s" % (T + 1, result[::-1])

if __name__ == '__main__':
	# debug = 0
	main()
