#!/usr/bin/env python
# encoding: utf-8
"""
c.py

Created by Yue Zhang on 2013-10-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	source = open('/Users/MnLeo/Desktop/c.in', 'r')
	output = open('/Users/MnLeo/Desktop/c.out', 'w')
	for T in range(int(source.readline())):
		N = int(source.readline())
		A = map(int, source.readline().split())
		B = map(int, source.readline().split())

		X = [[False] * N for i in xrange(N)]
		for i in range(N):
			for j in range(i + 1, N):
				if A[i] >= A[j]:
					X[i][j] = True
				if B[i] <= B[j]:
					X[j][i] = True
			
			# for some j < i with A[j] = A[i] - 1
			# one with the smallest X[j] is the largest j
			for j in range(i - 1, -1, -1):
				if A[j] == A[i] - 1:
					X[i][j] = True
					break
			for j in range(i + 1, N):
				if B[j] == B[i] - 1:
					X[i][j] = True
					break

		# for i in range(N):
		# 	print i, map(int, X[i])
		v = [0] * N
		r = 0
		while r < N:
			for i in range(N):
				if v[i] == 0 and \
				all(not X[i][j] or v[j] for j in xrange(N)):
					# print "i =", i
					v[i] = r + 1
					r += 1
					break

		# print "Case #%d: %s" % (T + 1, ' '.join(map(str, v)))
		output.write("Case #%d: %s\n" % (T + 1, ' '.join(map(str, v))))

if __name__ == '__main__':
	main()

