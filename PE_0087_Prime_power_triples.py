"""
Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power
"""

from time import perf_counter as tm

def primes_to(n):

	sieve=[1]*(n+1)
	primes = []
	for m in range(2,n+1):
		if sieve[m]:
			primes += [m]
			for j in range(m*m,n+1,m): sieve[j]=0
	return primes


def PE87(target):

	primes = primes_to(int(target**.5)+1)

	sqr = []
	cub = []
	frt = []
	for n in primes:
		n2 = n*n
		if n2 < target:
			sqr += [n2]
			n3 = n2*n
			if n3 < target:
				cub += [n3]
				n4 = n3*n
				if n4<target:
					frt += [n4]
		else: break

	print(*map(len,[sqr,cub,frt]))
	sqrfrt = set()
	for s in sqr:
		for f in frt:
			sf = s+f
			if sf<target:
				sqrfrt |= {sf}
			else: break

	sqrcubfrt = set()
	for s in sqrfrt:
		for c in cub:
			scf = s+c
			if scf<target:
				sqrcubfrt |= {scf}
			else: break
	return len(sqrcubfrt)

t = tm()
target = 50_000_000 # 29028
r = PE87(target)
print(r)
print(tm()-t)

