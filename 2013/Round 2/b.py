#!/usr/bin/env python
# encoding: utf-8
"""
b.py

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	def low_rank(n, p):
		if p == 0:
			return -1
		won = 0  # matches_won
		num = 2 ** n  # size_of_group
		while num > p:
			won += 1
			num /= 2
		return 2 ** n - 2 ** won

	source = open('b.in', 'r')

	for T in range(int(source.readline())):
		N, P = map(int, source.readline().split())
		print "Case #%d: %d" % (T + 1, \
			2 ** N - low_rank(N, 2 ** N - P) - 2, low_rank(N, P))

if __name__ == '__main__':
	main()
