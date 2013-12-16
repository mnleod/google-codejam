#!/usr/bin/env python
# encoding: utf-8
"""
a.py

Created by Yue Zhang on 2013-09-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
def solve(b):	
	for c in ['X', 'O']:
		wind1, wind2 = True, True
		for x in range(4):
			winh, winv = True, True
			for y in range(4):
				if b[y][x] != c and b[y][x] != 'T':
					winv = False
				if b[x][y] != c and b[x][y] != 'T':
					winh = False
			if winh or winv:
				return c + ' won'
			if b[x][x] != c and b[x][x] != 'T':
				wind1 = False
			if b[3 - x][x] != c and b[3 - x][x] != 'T':
				wind2 = False
		if wind1 or wind2:
			return c + ' won'

	for x in range(4):
		for y in range(4):
			if b[y][x] == '.':
				return 'Game has not completed'

	return 'Draw'

def main():
	source = open('a.in', 'r')
	# output = open('a.out', 'w')
	for T in range(int(source.readline())):
		b = []
		for l in range(4):
			b.append(list(source.readline().strip()))
		source.readline()
		print "Case #%d: %s" % ((T + 1), solve(b))


if __name__ == '__main__':
	main()
