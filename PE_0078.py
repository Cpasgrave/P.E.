"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

from collections import deque

def PE78(d):

	"""
	builds the triangle :
	0 1 2 3 4 5 6  7...

	1 0 0 0 0 0 0  0...
	  1 1 1 1 1 1  1...
	    2 2 3 3 4  4...
	      3 4 5 7  8...
	        5 6 9  11...
	          7 10 13...
	            11 14...
	               15...

	column by column, 
	keeps the bottom-most value for each column
	and check if it's a multiple of d.
	To build the next column, the process is to start from 0 at line 1
	And to add each number met by going diagonally left-down,
	then when the last number is met, add each last number of each column to the left.
	To save memory, this code keeps only what's needed: when only the last number of a 
	colmun will be needed, the column is turned into this number.

	"""

	triangle = [1,(0,1)]
	n = 3
	while True:
		col = [0,1]
		m = 1
		for i in range(2,n):
			t = triangle[-i]
			if isinstance(t,int): k = t
			else:
				if i >= len(t)-1:
					k = t[-1]
					triangle[-i] = k
				else:
					k = t[i]
			m += k
			col += [m]
		triangle += [col]
		print(m)
		if divmod(m,d)[1]==0:
			print(n-1)
			break
		n += 1

d = 100
# PE78(d)
# But this is not the way, it's finding the first multiple of 10 000 and 100 000, but 1 000 000 needs more memory than my computer has.


def P(d):
	# using Euler's algo with pentagonal numbers
	# https://en.wikipedia.org/wiki/Partition_(number_theory)
	# https://en.wikipedia.org/wiki/Pentagonal_number
	cache = [1,1]
	n = 2
	while True:
		s = 0
		m = n
		d1 = d2 = 1
		sign = 1 #(0:-,1:+)
		while m >= 0:
			m -= d1
			if m >= 0: s += cache[m] if sign else -cache[m]
			m -= d2
			if m >= 0: s += cache[m] if sign else -cache[m]
			sign = 1-sign
			d1 += 2
			d2 += 1
		cache += [s]
		n += 1
		if divmod(s,d)[1]==0: break
	return n-1,s

d = 1000000
r = P(d)
print(r)

