"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5²

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

### FIRST VERSION :



def euler9(n):

	triplet = (-1,0,0,0)
	print("hey")
	for a in range(1,(n-3)//3+1):
		a2 = a*a
		for b in range(a+1,(n-a)//2+1):
			c = n-a-b
			if a2+b*b==c*c:
				triplet = max(triplet,(a*b*c,a,b,c))
	return triplet

n = 3000
print(n)
e9 = euler9(n)
print(e9)
print()


### SECOND, MUCH MORE EFFICIENT

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
	while n>1:
		p = prm[i]
		while n%p==0:
			dec[p] = dec.get(p,0)+1
			n //= p
		i += 1
		if i==lp:
			if n!=1: dec[n] = 1
			break
	return dec

def divizors(prime_dec):
	divz = {1:{}}
	for k in prime_dec:
		new = {}
		for d in divz:
			for v in range(1,prime_dec[k]+1):
				new_d = d*k**v
				new[new_d] = dict(divz[d])
				new[new_d][k] = v
		divz.update(new)
	return divz

def euler9(n):

	"""
	based on : 
	n = a + b + c
	n = d x m x (m+n)
	we have - m and n coprimes
			- m > n
			- 2md and (m+n) coprimes

	the idea is to try all possible d,
	which are divizors of n
	then check all the distributions of factors to m and m+n
	respecting m > n, and m,n coprimes
	calculation of a x b x c equals to 2 x d^3 x (m^5n - n^5m)

	"""

	if n%2: return -1

	h = n//2
	pd = prime_dec(h)

	if sum(pd.values())<2 or [*pd.keys()]==[2]: return -1
	
	divs = divizors(pd)

	pairs = []
	for mnm,mnm_pd in divs.items():

		d = h//mnm

		for m in sorted(divizors(mnm_pd)):
			if m>=mnm**.5: break
			mn = mnm//m
			n = mn-m
			if n>=m: continue
			pairs += [(d**3*(m**5*n-m*n**5),d,m,n)]

	if pairs==[]: return -1
	abc,d,m,n = max(pairs)
	m2,n2 = m*m,n*n
	a,b,c = d*(m2-n2),2*d*m*n,d*(m2+n2)

	return a,b,c
		
n = 2*2*2*2*2*3*3*3*5*5*7*7*11*11*13*17*19
n = 75_256_855_804_676
print(n)

abc = euler9(n)
print(n,-1 if abc== -1 else f' - {abc} - {sum(abc)}')
if abc!=-1: 
	a,b,c = abc
	print(a*b*c)
