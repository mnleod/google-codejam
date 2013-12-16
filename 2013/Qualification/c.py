#!/usr/bin/env python
# encoding: utf-8
"""
c.py

Created by Yue Zhang on 2013-09-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
def dfs(num):
	def isFairSquare(num):
		if len(num) == 0:
			return True
		ixx = int(num)
		s = ixx * ixx
		p = str(s)
		if p == p[::-1] and s >= 10:
			result.append(s)
			return True
		elif s < 10:
			return False
		return False

	def cal(x):
		while True:
			xx = x + num + x[::-1]
			print xx
			ixx = int(xx)
			if ixx * ixx > MAX:
				break
			dfs(xx)
			x += '0'
	
	if not isFairSquare(num):
		return
	cal('1')
	cal('2')

def main():
	source = open('c.in', 'r')
	# output = open('c.out', 'w')
	for T in range(int(source.readline())):
		count = 0
		A, B = map(int, source.readline().split())
		for x in range(len(result)):
			if  B >= result[x] >= A:
				count += 1
			elif result[x] > B:
				break
		print "Case #%d: %d" % ((T + 1), count)


if __name__ == '__main__':
	result = [1, 4, 9]
	tt25 = 10**2#10**25
	MAX = 10**5#10**101
	for i in ['', '0', '1', '2']:
		dfs(i)
	result = sorted(result)
	main()

