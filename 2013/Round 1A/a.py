#!/usr/bin/env python
# encoding: utf-8
"""
a.py

Created by Yue Zhang on 2013-10-02.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	source = open('a.in', 'r')
	# output = open('a.out', 'w')
	for T in range(int(source.readline())):
		count = 0
		r, t = map(int, source.readline().split())
		res, lo, hi = 0, 1, t
		while lo <= hi:
			mid = (lo + hi) / 2
			if mid * (2 * r + 2 * mid - 1) > t:
				hi = mid - 1
			else:
				lo, res = mid + 1, mid
		print "Case #%d: %d" % (T + 1, res)


if __name__ == '__main__':
	main()

