#!/usr/bin/env python
# encoding: utf-8
"""
d.py

Created by Yue Zhang on 2013-09-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from collections import Counter

# For some test cases there are not sufficient keys present in the
# problem to unlock all of the chests.  This can be checked trivially
# before beginning the solution search.
def enough_keys_exist(chests, keys, key_req, keys_inside):
	keys_needed = Counter([key_req[c] for c in chests])
	keys_available = keys
	for c in chests:
		keys_available += keys_inside[c]
	for k in keys_needed:
		if keys_available[k] < keys_needed[k]:
			if debug:
				print "Need %d of key %d but only have %d" % (keys_needed[k], k, keys_available[k])
			return False  # no solution exists
	return True

# Verify that all needed key types may still be reachable
def still_possible(chests, keys, key_req, keys_inside):
	keys = set(keys)
	chests = chests.copy()

	def openable(chest):
		return key_req[chest] in keys

	openable_chests = filter(openable, chests)
	while openable_chests:
		for chest in openable_chests:
			keys |= set(keys_inside[chest])
			chests.remove(chest)
		openable_chests = filter(openable, chests)
	return not chests


def solve(chests, keys, key_req, keys_inside):
	# First check the global constraint to make sure a solution isn't
	# obviously impossible
	if not enough_keys_exist(chests, keys, key_req, keys_inside):
		return False, None

	# Make sure all keys are potentially reachable
	if not still_possible(chests, keys, key_req, keys_inside):
		return False, None

	solution = []

	for position in range(len(chests)):
		for c in sorted(chests):
			# Skip this chest if we can't open it:
			if not key_req[c] in keys:
				continue
			# Open the chest:
			keys[key_req[c]] -= 1
			chests.remove(c)
			keys += keys_inside[c]
			# Make sure there's still a way to obtain all needed keys:
			if still_possible(chests, keys, key_req, keys_inside):
				break
			# Re-wind before trying the next chest
			chests.add(c)
			keys -= keys_inside[c]
			keys[key_req[c]] += 1
		else:
			# Could not open any chest --> no solution
			# This code will never be reached!
			print "FAIL"
			return False, None  

		solution.append(c)

	return True, solution

def main():
	source = open('/Users/MnLeo/Desktop/d.in', 'r')
	# output = open('d.out', 'w')
	for T in range(int(source.readline())):
		K, N = map(int, source.readline().split())
		keys = Counter(map(int, source.readline().split()))

		key_req = {}
		keys_inside = {}
		for n in range(1, N + 1):
			numbers = map(int, source.readline().split())
			key_req[n] = numbers[0]
			keys_inside[n] = Counter(numbers[2:])
		chests = set(range(1, N + 1))
		
		if debug:
			print chests, keys, key_req, keys_inside

		solution_exists, solution = solve(chests, keys, key_req, keys_inside)

		if solution_exists:
			print "Case #%d: %s" % ((T + 1), " ".join(map(str,solution)))
		else:
			print "Case #%d: %s" % ((T + 1), "IMPOSSIBLE")



if __name__ == '__main__':
	debug = 0
	main()
