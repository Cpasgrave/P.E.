'''
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
from time import perf_counter as time

t = time()
target = 0,0
for p in range(2,1001,2): # only pair perimeters can be a+b+c with c²=a²+b²
	n = 0
	for a in range(2,p//4+1):
		if (p*p-2*p*a)%(2*(p-a)): continue
		# from a+b+c=p and c²=a²+b², it's easy to get the formula:
		# b = (p*p-2*p*a)%(2*(p-a)), so when b integer, c and p will also be integers.
		else: n += 1
	if n>target[0]:
		target = n,p

print(target) # 840
print(time()-t)
