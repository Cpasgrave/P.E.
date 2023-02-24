"""
Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from functools import cache
from time import perf_counter as tm
import sys


# solution naïve (trop lent pour n=100):

def E76(n):
	
	if n<2:	return 0
	if n==2: return 1

	# set de tuples qui représentent la décomposition d'entiers
	# démarre avec (0,2) -> aucun 0, deux 1 = 2*1 = 2
	# par ex : (0,1,0,0,1)
	ct = {(0,2)}

	for i in range(3,n+1):
		# on progresse de 3 à n en se servant du précédent pour former le suivant

		new = set()
		for c in ct: # a chaque n+1, on prend les précédentes décompositions
					 # et pour chacune on ajoute un 1
			new |= {tuple(e+1 if i==1 else e for i,e in enumerate(c))}
		# on ajoute aussi l'élément (0,1,...,1) pour la décomposition : 1 + (n-1)
		new |= {tuple(j if j<2 else 1 if j==i-1 else 0 for j in range(i))}
		ct = new

		new = set()
		for c in ct: # ensuite, pour chaque décomposition qui a plus d'un 1 
					 # et qui est composée d'autre entiers
					 # on transforme les 1 en leur somme
					 # ex : 1 + 1 + 1 + 2 + 3 ou (0,3,1,1) devient 2 + 3 + 3 ou (0,0,1,2)
			lc = len(c)
			if lc>2:
				n1 = c[1]
				if n1>1:
					c = list(c)
					c[1] = 0
					c = c + [0 for i in range(n1+1-lc)]
					c[n1] += 1
					c = tuple(c)
					new |= {c}
		ct |= new

	return len(ct)




@cache
def E76b(n,m=0):
	# the idea behind this code is :
	# n becomes 1+1+1+...+1 (n ones)
	# this counts for 1 sum
	# then, for k starting with 2, up to n, ones will be turned into k
	# ex:
	# n = 6
	# n = 1+1+1+1+1+1 (ct = 1)
	# k = 2
	# n = 2+1+1+1+1
	# ct += 1 + F(1+1+1+1,2)
	# a recursion will calculate the possible number of sums that can be done, keeping the first 2
	# but for these recursions, k will have a minimum value.
	# because here, 2+3+1 will be counted from the recursion after k=2
	# so when k=3, the recursion will only count 3+3 (and not 3+2+1 twice)

	if not m:
		if n<2: return 0
		m = 2
	elif n<m: return 0

	ct = 1
	for k in range(m,n):
		nk = n-k
		ct += E76b(nk,k) + 1

	return ct


n = 100
sys.setrecursionlimit(n*3)

t = tm()
r = E76b(n)
print(r)
print(tm()-t)


def E76c(n):

	ct = [1]+[0]*n
	for i in range(1,n):
		for j in range(i, n+1):
			ct[j] += ct[j-i]

	return ct[-1]

n = 100

t = tm()
r = E76c(n)
print(r)
print(tm()-t)



# nouvelle approche:
"""
    1   2   3   4   5   6   7 (i)   total
 1  1                             1
 2  1   1                         2
 3  1   1   1                     3
 4  1   2   1   1                 5
 5  1   2   2   1   1             7
 6  1   3   3   2   1   1        11
 7  1   3   4   3   2   1   1    15
 8  ....
(n)

P(n):
x = n-i
if x<=i: ith term = total P(x)
else:    ith term = sum of first i terms of P(x)

(The nth term is always = 1, i.e. when x=0)
"""

# @cache
# def PE76d(n,k):
# 	if n==k: return PE76d(n,k-1)+1
# 	if k==0 or n<0: return 0
# 	if n==0: return 1
# 	return PE76d(n,k-1) + PE76d(n-k,k)

# n = 100

# t = tm()
# r = PE76d(n,n)
# print(r)
# print(tm()-t)

sys.setrecursionlimit(10000)

@cache
def PE76e(n):
	# méthode Euler https://en.wikipedia.org/wiki/Partition_(number_theory)
	if n<0: return 0
	if n in {0,1}: return 1
	s = 0
	m = n
	d1 = d2 = 1
	sign = 1 #(0:-,1:+)
	while m>0:
		m -= d1
		p = PE76e(m)
		m -= d2
		p += PE76e(m)
		s = s+(p if sign else -p)
		sign = 1-sign
		d1 += 2
		d2 += 1
	return s

t = tm()
r = PE76e(n)
print(r)
print(tm()-t)



