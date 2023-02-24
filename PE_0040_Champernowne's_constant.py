'''
Champernowne's constant

An irrational decimal fraction is created
by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
from time import perf_counter as time

t = time()
step = (s for s in[1,10,100,1000,10000,100000,1000000])
nd = 0

s = next(step)
exp = []
for digs in range(6):
	for n in range(10**digs,10**(digs+1)):
		nd += digs+1
		if nd >= s:
			exp.append(int(str(n)[s-nd-1]))
			if nd > 1000000: break
			s = next(step)

print(len(exp),exp)
res = 1
for e in exp:
	res *= e
print('result = ',res) # 210
print(time()-t) # 0.095739
