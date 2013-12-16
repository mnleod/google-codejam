#!/usr/bin/env python
# encoding: utf-8
"""
c.py

http://www.cnblogs.com/AnnieKim/archive/2013/05/08/3059614.html

Created by Yue Zhang on 2013-10-08.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import copy
import math
class EOW(object):
	"""End-of-word marker."""
	def __repr__(self):
		return '$'
EOW = EOW()

class iddict(dict):
	def __hash__(self):
		return id(self)

def prefix_tree(words):
	"""Build a prefix tree representing a set of words."""
	d = iddict()
	for word in words:
		t = d
		for c in word:
			t = t.setdefault(c, iddict())
		t[EOW] = iddict()  # mark end of word
	return d

def solve(s):
	n = len(s)
	penalty = sys.maxint >> 1

	cache = {None: 0}
	root = (0, 0, words)
	stack = [(root, 0, root)] 

	while stack:
		dest, incr, cell = job = stack.pop()
		# if the answer to this job is known, use it
		if cell in cache:
			cache[dest] = min(cache.get(dest, penalty), cache[cell] + incr)
			continue
		# otherwise, expand this job into its subjobs and let them run
		stack.append(job)
		stack.append([cell, penalty, None]) # default the cell to a dead end
		i, subst, tree = cell

		# is the end of the message?
		if i == n:
			cache[cell] = 0 if EOW in tree else penalty
			continue
		# is there a possible word ending here?
		if EOW in tree:
			stack.append([cell, 0, (i, subst, words)])
		# is the current char part of a dictionary word?
		if s[i] in tree:
			stack.append([cell, 0, (i + 1, max(0, subst - 1), tree[s[i]])])
		# can we change the current char to part of a dictionary word?
		if subst == 0:
			for l in letters:
				if l != s[i] and l in tree:
					stack.append([cell, 1, (i + 1, 4, tree[l])])
	return cache[root]

def main():
	pass
		
if __name__ == '__main__':
	letters = ''.join(chr(i) for i in xrange(ord('a'), ord('z') + 1))
	source = open('c.in', 'r')
	words = prefix_tree([line.strip() for line in open('dict.txt', 'r')])

	for T in range(int(source.readline())):
		mem = [[-1] * 10] * 50
		s = source.readline().strip()
		print "Case #%d: %d" % (T + 1, solve(s))

	# main()