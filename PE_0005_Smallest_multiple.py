"""
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to n ?

1 <= n <= 40
"""
from functools import reduce
from operator import mul

def primes_to(n):
	sieve=[1]*(n+1)
	primes = []
	for m in range(2,n+1):
		if sieve[m]:
			primes += [m]
			for j in range(m*m,n+1,m): sieve[j]=0
	return primes

def prime_dec(n):
	dec = {}
	prm = primes_to(int(n**.5)+1)
	lp = len(prm)
	i = 0
	while n!=1:
		p = prm[i]
		while n%p==0:
			dec[p] = dec.get(p,0)+1
			n //= p
		i += 1
		if i==lp: 
			dec[n] = 1
			break
	return dec

def smallest_multiple(n):
	if n==1: return n
	div = {}
	for m in range(2,n+1):
		pdm = prime_dec(m)
		for p,n in pdm.items():
			div[p] = max(div.get(p,0),n)
	return reduce(mul,[k**v for k,v in div.items()])

for n in range(1,41):
	sm = smallest_multiple(n)
	print(n,sm)
