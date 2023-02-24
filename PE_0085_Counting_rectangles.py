"""
Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

def rectangles_count(M,N):

	ct = 0
	for m in range(M):
		for n in range(N):
			ct += (M-m)*(N-n)
	return ct



def PE85(target):

	M = 1
	while True:
		n = rectangles_count(M,M)
		if n>target: break
		M += 1
	N = M
	solutions = {}
	diff = n-target
	solution = (diff,M,N)
	
	while True:
		# lower N
		while True:
			N -= 1
			diff = rectangles_count(M,N)-target
			solution = min((abs(diff),M,N),solution)
			if diff<0: break
		if N==0: break
		# grow M
		while True:
			M += 1
			diff = rectangles_count(M,N)-target
			solution = min((abs(diff),M,N),solution)
			if diff>0: break
	d,m,n = solution
	return rectangles_count(m,n),d,m,n,m*n

t = 2000000
r = PE85(t)
print(r)
