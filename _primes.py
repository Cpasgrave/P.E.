

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
	prm = primesTo(int(n**.5)+1)
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

def divizors(prime_d):
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

def pFac(n):
    fac = dd(int)
    while n%2==0:
        n //= 2
        fac[2] += 1
    p = 3
    while p <= n:
        if n%p==0:
            n //= p
            fac[p] += 1
        else: p += 2
    return [(k,v) for k,v in fac.items()]



def div(n):
    F = pFac(n)
    divs = {1}
    for p,pow in F:
        for _ in range(pow):
            for v in set(divs):
                divs.add(p*v)
    return divs

