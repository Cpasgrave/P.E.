'''
Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
from time import perf_counter as time

t = time()
P = []
pan10 = {1,2,3,4,5,6,7,8,9,0}
for d1 in pan10:
	for d2 in pan10-{d1}:
		for d3 in pan10-{d1,d2}:
			for d4 in {2,4,6,8,0}-{d1,d2,d3}:
				mod3 = (d3+d4)%3
				s = {0} if mod3==0 else set()
				for d5 in s|{3-mod3+3*i for i in range(3)}-{d1,d2,d3,d4}:
					for d6 in {0,5}-{d1,d2,d3,d4,d5}:
						for d7 in [d for d in pan10-{d1,d2,d3,d4,d5,d6} if (d5*100+d6*10+d)%7==0]:
							for d8 in [d for d in pan10-{d1,d2,d3,d4,d5,d6,d7} if (d6*100+d7*10+d)%11==0]:
								for d9 in [d for d in pan10-{d1,d2,d3,d4,d5,d6,d7,d8} if (d7*100+d8*10+d)%13==0]:
									for d10 in [d for d in pan10-{d1,d2,d3,d4,d5,d6,d7,d8,d9} if (d8*100+d9*10+d)%17==0]:
										P.append(d1*10**9+d2*10**8+d3*10**7+d4*10**6+d5*10**5+d6*10**4+d7*10**3+d8*10**2+d9*10**1+d10)

print(len(P))
print(sum(P)) # 16695334890

print(time()-t)
