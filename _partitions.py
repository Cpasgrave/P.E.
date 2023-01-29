from time import perf_counter as tm

# all possible partitions, preserved order
def part_ord(a):
	if len(a)==1: yield [a];return
	a0 = a[0]
	for p in part_ord(a[1:]): 
		yield [[a0]+p[0]]+p[1:]
		yield [[a0],*p]

# all possible partitions, all orders
def part(a):
	if len(a)==1: yield [a];return
	a0 = a[0]
	for p in part(a[1:]): 
		yield [[a0],*p]
		for i in range(len(p)):
			yield p[:i]+[[a0]+p[i]]+p[i+1:]

# all k-long
def part_k(a,k):
	if k==1: yield [a]
	elif len(a)>1:
		a0 = [a[0]]
		for p in part_k(a[1:],k-1):	yield [a0]+p
		for p in part_k(a[1:],k):
			for i in range(k): yield p[:i]+[a0+p[i]]+p[i+1:]

# same, bit faster
def partition_k(a,k,m=None):
	if m==None: m=k
	if len(a)>1:
		for p in partition_k(a[1:],k,m-1):
			lp = len(p)
			if lp>k: continue
			if lp>=m:
			  for n, subset in enumerate(p): yield p[:n]+[[a[0]]+subset]+p[n+1:]
			if lp<k: yield [[a[0]]]+p
	else: yield [a]



a = [1,2,3,4]
k = 3

t = tm()
pk = [*part_ord(a)]
print(tm()-t)
print(len(pk))
print(pk)

t = tm()
pk = [*part(a)]
print(tm()-t)
print(len(pk))
print(pk)

t = tm()
pk = [*part_k(a,k)]
print(tm()-t)
print(len(pk))
print(pk)