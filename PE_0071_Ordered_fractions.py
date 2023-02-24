"""
Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""
from random import choice
from fractions import Fraction as F
from math import gcd

def diophantine(a,b,c):
	if c%gcd(a,b): return None
	m,n,p,q=1,0,0,1
	while a%b!=0:
		dv,md = divmod(a,b)
		a,b,q,p,n,m = b,md,p-(q*dv),q,m-(n*dv),n
	return n*c,q*c


############# Essayer directement la comparaison de fractions

def fracNear(n,d,limit,start=1):

	target = n/d

	bf,af = -float('inf'),float('inf')
	before,after = [(bf,0)]*11,[(af,0)]*10
	
	for den in range(start,limit+1):
		num = n*den//d
		fracinf = num/den
		fracsup = (num+1)/den

		if fracinf>bf:
			fracinf = (fracinf,F(num,den))
			if fracinf not in before:
				before = sorted(before+[fracinf])
				bf = before.pop(0)[0]

		if fracsup<af:
			fracsup = (fracsup,F(num+1,den))
			if fracsup not in after:
				after = sorted(after+[fracsup])
				af = after.pop()[0]			

	for f in [b[1] for b in before]+[a[1] for a in after]:
		print(f"{str(f):^{len(str(limit))*2+1}}->{float(f):>{len(str(int(n/d)))+16}.14f}")
	print(*[f"{str(f)}" for f in [b[1] for b in before]+[a[1] for a in after]],sep=', ')


def fracNear3(num,den,limit):
	# last ancestors method 
	# bugs
	frac = F(num,den)
	num = frac.numerator
	den = frac.denominator
	N = num/den

	LowerAncestor = (0,1)
	HigherAncestor = (1,0)
	n1,d1,n2,d2,n3,d3 = 0,1,1,1,1,0
	while True:
		if N>n2/d2:
			n1,d1,n2,d2 = n2,d2,n2+n3,d2+d3
			if num==n2 and den==d2: break
			LowerAncestor = (n2,d2)
		else:
			n2,d2,n3,d3 = n1+n2,d1+d2,n2,d2
			if num==n2 and den==d2: break
			HigherAncestor = (n2,d2)

	na,da = LowerAncestor
	dm = (limit//den)*den
	if dm+da<N: dm += da
	else: dm = dm-den+da
	nm = num*dm//den
	return nm,dm
	
def fracNear4(num,den,limit,iter):
	A = [(num,den)]

	for i in range(iter):

		for side in [0,-1]:
			sn,sd = A[side]
			if sd==0: continue
			if i: limit = sd
			frac = F(sn,sd)
			sn,sd = frac.numerator,frac.denominator
			best = [(0,0,0),(float('inf'),0,0)][side]
			Q = sn/sd

			# print(max(limit-den-1,1))
			for d in range(limit,max(limit-den-1,1),-1):
				n = d*sn//sd-side
				q = n/d
				if q!=Q: best = sorted([best,(q,n,d)])[side+1]
			A.insert(side==-1 and len(A)+1,best[1:])

	return [F(*a)for a in A if a[1]!=0]

from math import gcd
def fracNear5(num,den,limit,n):

	f = num/den

	a,b = 0,1
	y,z = 1,0
	left = [(0,0)]*n
	right = [(0,0)]*n

	while True:
		a,b = a+num,b+den
		if b>limit: break
		gcdab = gcd(a,b)
		if gcdab != 1:
			a //= gcdab
			b //= gcdab
		ab = a/b
		left = left[1:]+[(a,b)]

	while True:
		y,z = y+num,z+den
		if z>limit: break
		gcdyz = gcd(y,z)
		if gcdyz != 1:
			y //= gcdyz
			z //= gcdyz
		yz = y/z
		right = [(y,z)]+right[:-1]

	return left+[(num,den)]+right



n = 301
d = 7021
limit = 10000
iter = 10
fracNear(n,d,limit)
# print()
# fracNear2(n,d,limit)
# print()
# A = fracNear4(n,d,limit,iter)
# print(*[f"{str(a):^{len(str(limit))*2+1}} -> {float(a):>{len(str(int(n/d)))+16}.14f}"for a in A],sep='\n')
# print()
# print(*A,sep=', ')
# # print(l)
# print()
# print(*r,sep=', ')
# print(r)

A = fracNear5(n,d,limit,10)
print(A)