'''
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from time import perf_counter as time

def PM():
	best = 0
	pand9 = {'1','2','3','4','5','6','7','8','9'}
	for i in range(3,9):
		R = list(range(1,i))
		lR = len(R)
		for n in range(10**(9//lR-1),10**(9//lR)):
			concat = ''
			for r in R:
				concat += str(n*r)
			if len(concat)==9:
			  if set(concat)==pand9:
			    concat = int(concat)
			    best = max(best,concat)

	return best

t = time()

print(PM())  # 932718654

print(time()-t)
