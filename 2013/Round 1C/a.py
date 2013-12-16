#!/usr/bin/env python
# encoding: utf-8
"""
a.py

https://code.google.com/codejam/contest/2437488/dashboard#s=a&a=0

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	source = open('a.in', 'r')
	for T in range(int(source.readline())):
		s, n = source.readline().split()
		l = len(s)
		n = int(n)
		r, c, count = 0, 0, 0
		for i in range(l):
			c = c + 1 if s[i] not in "aeiou" else 0	
			if c >= n:
				# so if x letters are counted earlier then our r will become r – x
				count += (i - n - r + 2) * (l - i)
				r = i - n + 2 # additional 1 for no letter
				print "r, s =", r, s

		print "Case #%d: %d" % (T + 1, count)

if __name__ == '__main__':
	main()

