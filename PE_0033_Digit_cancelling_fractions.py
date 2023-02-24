'''
Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest
common terms, find the value of the denominator.
'''

den = []
for n in range(10,100):
	for d in range(n+1,100):
		for c in '123456789':
			sn = str(n)
			sd = str(d)
			if any(c not in s for s in (sn,sd)): continue
			fr = n/d
			try:
				nc = int(sn.replace(c,''))
				dc = int(sd.replace(c,''))
				cc = nc/dc
			except:
				continue
			if fr == cc:
				den.append(dc)
				print(n,d,nc,dc)

res = 1
for d in den:
	res *= d
print(res)

'''
16 64 1 4
19 95 1 5
26 65 2 5
49 98 4 8

8
800

100
'''
