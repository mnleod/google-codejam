#!/usr/bin/env python
# encoding: utf-8
"""
c2.py

http://caethan.wordpress.com/2013/05/17/gcj-garbled-email/

Created by Yue Zhang on 2013-10-11.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import numpy

def precalculate():
	
	global tree
	global end

	tree = {}
	end = ''

	def add_branch(tree, word):
		for char in word:
			if not char in tree:
				tree[char] = {}
			tree = tree[char]
		tree[end] = True

	infile = open('words.txt')
	for line in infile.readlines():
		add_branch(tree, line.strip())
	infile.close()

def match_words(S, prefix, index, required):
	suffix = S[index:]

	#Walk down the tree to find the right branch
	branch = tree
	for char in prefix:
		branch = branch[char]

	if suffix == '':
		return 0 if end in branch else -1

	def check(best, new, inc = 0):
		if new == -1:
			return best
		if best is None:
			best = new + inc
		else:
			best = min(best, new + inc)
		return best

	print "suffix =", suffix

	best = None

	char = suffix[0]
	if char in branch: #valid match
		if end in branch[char]: #end of a word
			best = check(best, mincosts[index + 1, max(0, required - 1)])
		print "1. best =", best, S, prefix + char, index + 1, max(0, required - 1)
		best = check(best, match_words(S, prefix + char, index + 1, max(0, required - 1)))
		print "2. best =", best 
	if required == 0:
		for this in branch:
			if this == end or this == char:
				continue
			if end in branch[this]:
				best = check(best, mincosts[index + 1, 4], 1)
			print "3. best =", best 
			if best is None or best > 1: #Don't bother checking if best is already good enough
				best = check(best, match_words(S, prefix + this, index + 1, 4), 1)
			print "4. best =", best 
	return -1 if best is None else best

def main():
	source = open('c.in', 'r')
	for T in range(int(source.readline())):
		S = source.readline().strip()
		
		global mincosts
		mincosts = numpy.zeros((len(S) + 1, 5), dtype=int)

		for index in range(len(S))[::-1]:
			for required in range(5):
				mincosts[index, required] = match_words(S, '', index, required)
		
		print mincosts

		print "Case #%d: %d" % (T + 1, mincosts[0,0])

if __name__ == '__main__':
	#We're going to load the dictionary into a trie
	precalculate()
	main()