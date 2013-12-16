#!/usr/bin/env python
# encoding: utf-8
"""
c.py

https://code.google.com/codejam/contest/2437488/dashboard#s=a&a=2

small:
http://martin-thoma.com/google-code-jam-round-1c-2013/

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import math

def main():
	source = open('c.in', 'r')

	for T in range(int(source.readline())):
	# d[i] – the day of the tribe's first attack (where 1st January, 250BC, is considered day 0)
	# n[i] – the number of attacks from this tribe
	# w[i], e[i] – the westmost and eastmost points respectively of the Wall attacked on the first attack
	# s[i] – the strength of the first attack
	# delta_d[i] – the number of days between subsequent attacks by this tribe
	# delta_p[i] – the distance this tribe travels to the east between subsequent attacks
	#  (if this is negative, the tribe travels to the west)
	# delta_s[i] – the change in strength between subsequent attacks
		d, n, w, e, s = [], [], [], [], []
		delta_d, delta_p, delta_s = [], [], []
		for N in range(int(source.readline())):

		# print "Case #%d: %d" % (T + 1, solve(s))

if __name__ == '__main__':
	main()
