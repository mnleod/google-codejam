#!/usr/bin/env python
# encoding: utf-8
"""
b.py

Created by Yue Zhang on 2013-09-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import numpy as np

def solve(n, m, lines):
	# find max value per row
	nMax = map(max, lines)

	# find max value per column
	mMax = [reduce(max, [lines[i][j] for i in range(n)]) for j in range(m)]

	# YES, if: A(n,m) >= the colMax or rowMax
	for i in range(n):
		for j in range(m):
			if lines[i][j] < nMax[i] and lines[i][j] < mMax[j]:
				return "NO"
	return "YES"


def main():
	source = open('b.in', 'r')
	# output = open('b.out', 'w')
	for T in range(int(source.readline())):
		N, M = map(int, source.readline().split())
		lawn = [map(int, source.readline().split()) for x in range(N)]
		print "Case #%d: %s" % ((T + 1), solve(N, M, lawn))

if __name__ == '__main__':
	main()
