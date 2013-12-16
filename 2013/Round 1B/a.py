#!/usr/bin/env python
# encoding: utf-8
"""
a.py

Created by Yue Zhang on 2013-10-07.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	source = open('a.in', 'r')
	# output = open('a.out', 'w')
	for T in range(int(source.readline())):
		count = 0
		A, N = map(int, source.readline().split())
		motes = sorted(map(int, source.readline().split()))

		mine, best = 0, N
		if not A == 1:	
			for index, i in enumerate(motes):
				# print index, i, A
				if i < A:
					A += i
					continue
				# consider N+1 cases -- try to absorb 0, 1, ... N 
				# of the original motes and remove the remainder
				best = min(best, mine + N - index)

				while A <= i:
					A += A - 1
					mine += 1
				A += i
			best = min(best, mine)
		print "Case #%d: %d" % (T + 1, best)

if __name__ == '__main__':
	main()

