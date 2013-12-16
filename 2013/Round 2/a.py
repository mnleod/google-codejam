#!/usr/bin/env python
# encoding: utf-8
"""
a.py

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def main():
	def cal_fee(n):
		return ( N + N - n + 1) * n / 2
	source = open('a.in', 'r')
	# output = open('/Users/MnLeo/Desktop/a.out', 'w')
	for T in range(int(source.readline())):
		N, M = map(int, source.readline().split())
		total = 0
		events, tickets = [], []
		for m in range(M):
			o, e, p = map(int, source.readline().split())
			events.append((o, 0, p))
			events.append((e, 1, p))
			total += p * cal_fee(e - o)
		events.sort()
		
		# tp, timepoint; t, type; a, amount 
		for tp, t, a in events:
			if t == 0:
				tickets.append([tp, a])
			else:
				s = a
				while s > 0:
					if tickets[-1][1] == 0:
						tickets.pop()
					t = min(tickets[-1][1], s)
					s -= t
					tickets[-1][1] -= t
					total -= t * cal_fee(tp - tickets[-1][0])
				
		print "Case #%d: %d" % (T + 1, total % 1000002013)
		# output.write("Case #%d: %d\n" % (T + 1, total % 1000002013))


if __name__ == '__main__':
	main()
