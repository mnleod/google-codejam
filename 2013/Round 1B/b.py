#!/usr/bin/env python
# encoding: utf-8
"""
b.py

http://stackoverflow.com/questions/16388954/google-code-jam-2013-r1b-falling-diamonds

Created by Yue Zhang on 2013-10-07.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	"""
	k         0      1          3            5  ...
	Full      1      6         15           28  ...

											 ◆
										    ◆ ◆
							    ◆          ◆ ◆ ◆
							   ◆ ◆        ◆ ◆ ◆ ◆
					 ◆        ◆ ◆ ◆      ◆ ◆ ◆ ◆ ◆
					◆ ◆      ◆ ◆ ◆ ◆    ◆ ◆ ◆ ◆ ◆ ◆
			  ◆    ◆ ◆ ◆    ◆ ◆ ◆ ◆ ◆  ◆ ◆ ◆ ◆ ◆ ◆ ◆
	"""
	# binomial coefficient
	def binom(n, r):
		p = 1.0
		for i in range(r):
			p = p * (n - i) / (i + 1)
		return p

	source = open('b.in', 'r')
	# output = open('b.out', 'w')
	for T in range(int(source.readline())):
		count = 0
		# the number of falling diamonds N,
		# the position X, Y of the place you are interested in 
		N, X, Y = map(int, source.readline().split())

		k = 1 # 
		while (k + 2) * (k + 3) / 2 <= N:
			k += 2
		assert k % 2 == 1
		
		# one of the N diamonds will fall so that its center 
		#  ends up exactly at (X, Y)
		# find out which level is
		level = abs(X) + Y + 1
		assert level % 2 == 1
		
		# X, Y in the pyramid built by N diamonds
		if level <= k:
			print "Case #%d: 1.0" % (T + 1)
			continue
		# X, Y out of the pyramid built by N diamonds
		if level > k + 2:
			print "Case #%d: 0.0" % (T + 1)
			continue

		# N diamonds will start to fill the next bigger pyramid
		# calculate overflow = N - k * (k + 1) / 2
		assert level == k + 2
		d = N - k * (k + 1) / 2
		h = k + 1
		assert d <= 2 * h

		if Y == h:
			print "Case #%d: 0.0" % (T + 1)
			continue

		if d > h and Y < d - h:
			print "Case #%d: 1.0" % (T + 1)
			continue

		# The general algorithm is to assume, 
		# that the last 0, 1, 2, 3, ..., nr elements will go to 
		# the right side inevitably, then to calculate 
		# the probability for each of these cases 
		# (the last 0, 1, 2, 3, ..., nr probabilites will be 1) and 
		# multiply each probability with the number of different cases 
		# where the last 0, 1, 2, 3, ..., nr probabilities are 1.
		prob = 0.0
		for i in range(Y + 1, d + 1):
			prob += binom(d, i)
		prob /= 2**d
		print "Case #%d: %f" % (T + 1, prob)

if __name__ == '__main__':
	# debug = 0
	main()
