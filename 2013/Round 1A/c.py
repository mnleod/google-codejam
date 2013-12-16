#!/usr/bin/env python
# encoding: utf-8
"""
c.py
 
http://www.cnblogs.com/AnnieKim/archive/2013/05/08/3059614.html

Created by Yue Zhang on 2013-10-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import copy
import math


# all possible combinations 
def comb(N, M):
	digits = []
	digit = [2] * N
	while not digit == [M] * N:
		digits.append(copy.copy(digit))
		i = N - 1
		while digit[i] == M: i -= 1
		digit[i] += 1
		for j in range(i + 1, N):
			digit[j] = digit[i]
	digits.append(digit)
	return digits

# Pascal's triangle
def pascal(M):
	C = [[0] * M for i in range(M)]
	C[0][0] = 1
	for i in range(1, M):
		C[i][0] = 1
		for j in range(1, i+1):
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
			if debug: print "C[%d][%d] = %d" % (i, j, C[i][j])
	return C

# calculate the probability of combination
def prob(D, C, N, M , t):
	prob = [0] * t
	for i in range(t):
		count = [0] * (M + 1)
		for j in range(N):
			count[D[i][j]] += 1
		p = 0
		size = N
		for j in range(2, M):
			p += math.log(C[size][count[j]])
			size -= count[j]
		prob[i] = p
	return prob

# list all possible products
def products(D, N, t):
	products = [{}] * t
	for i in range(t):
		products[i] = {}
		for mask in range(1, 1 << N):
			prod = 1
			for j in range(N):
				if mask & (1 << j):
					prod *= D[i][j]
			if products[i].has_key(prod):
				products[i][prod] += 1
			else:
				products[i][prod] = 1
	return products

def main():
	source = open('c.in', 'r')
	for T in range(int(source.readline())):
		count = 0
		R, N, M, K = map(int, source.readline().split())
		D = comb(N, M)
		L = len(D)
		C = pascal(M)
		P = prob(D, C, N, M , L)
		X = products(D, N, L)
 		
 		print "Case #%d:" % (T + 1)
		
		for r in range(R):
			ps = map(int, source.readline().split())
			res = 0
			res_prob = INT_MIN

			for i in range(L):
				p = P[i]
				for n in ps:
					if n == 1:
						break
					if n in X[i]:
						p += math.log(X[i][n])
					else:
						p = INT_MIN
						break
				if res_prob < p:
					res = i
					res_prob = p
			print "".join(str(x) for x in D[res])
		
if __name__ == '__main__':
	debug = 0
	INT_MIN = -1 * sys.maxint
	main()
	# print pascal(4)