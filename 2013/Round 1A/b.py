#!/usr/bin/env python
# encoding: utf-8
"""
b.py

Created by Yue Zhang on 2013-10-02.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	"""
	If we can spend any energy, and still have E energy
	 when X comes (assuming we don't spend any between now and X),
	 spend as much as we can while still having E when X comes.
	If we can't spend any energy and still have E when X comes,
	 we shouldn't spend all our energy will be better spent at X.
	"""
	source = open('b.in', 'r')
	# output = open('b.out', 'w')
	for T in range(int(source.readline())):
		count = 0
		# E, the maximum (and initial) amount of energy,
		# R, the amount you regain after each activity, and
		# N, the number of activities planned for the day
		E, R, N = map(int, source.readline().split())
		V = map(int, source.readline().split())

		answer = 0
		amount, gain = [E], [V[0]]

		for n in range(1, N):
			if debug:
				print "1. amount, gain, answer = ", amount, gain, answer
			take = R

			while take > 0:
				if amount == []:
					break
				if amount[0] > take: # use R * V[i]
					answer += gain[0] * take
					amount[0] -= take
					take = 0
				else: # if all engergy
					answer += gain[0] * amount[0]
					take -= amount[0]
					amount.pop(0)
					gain.pop(0)
			if debug:
				print "  2. amount, gain, answer = ", amount, gain, answer
			add = R
			# if there is no more important activity in further, keep
			#  and add this part in above code 
			while not gain == [] and gain[-1] <= V[n]:
				add += amount.pop(-1)
				gain.pop(-1)
			if debug:
				print "   3. amount, gain, answer = ", amount, gain, answer
			amount.append(add)
			gain.append(V[n])
		if debug:
			print "    4. amount, gain, answer = ", amount, gain, answer
		while not gain == []:
			answer += amount.pop(0) * gain.pop(0)

		print "Case #%d: %d" % (T + 1, answer)


if __name__ == '__main__':
	debug = 0
	main()
