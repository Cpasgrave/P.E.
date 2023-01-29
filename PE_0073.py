from math import ceil

def fracount(limit):

	avoid = {n:set() for n in range(4,limit+1)}
	ct = 0
	
	for d in range(4,limit+1):
		left = d//3 + 1
		right = ceil(d/2)
		av = avoid[d]
		for n in range(left,right):
			if n in av: continue
			ct += 1
			mul = 2
			dm = d*mul
			while dm <= limit:
				avoid[dm] |= {n*mul}
				mul += 1
				dm = d*mul

	return ct

limit = 120000

print(fracount(limit))
