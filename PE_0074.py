"""
EULER 74

The number 145 is well known for the property that 
the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces 
the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number 
will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number 
below one million is sixty terms.

How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?
"""

from math import factorial

rg10 = range(10)
rg9 = range(9)
rg8 = range(8)
fac = [factorial(n) for n in range(1,10)]

def tree_add(tree,decaN,size):
	node = tree
	for i in rg8:
		value = decaN[i]
		if not node[value]: node[value] = [None,None,None,None,None,None,None,None]
		node = node[value]
	value = decaN[8]
	node[value] = size

def tree_check(tree,decaN):
	node = tree
	for i in rg9:
		value = decaN[i]
		if node[value]==None: return None
		node = node[value]
	return node

def decaN(n):
	D = [0]*9
	while n:
		n,m = divmod(n,10)
		D[m-1 if m else 0] += 1
	return D

def next_deca(d):
	s = 0
	for i in rg9:
		s += d[i]*fac[i]
	return decaN(s)

def euler74(limit,target):

	Tree = [None]*8

	ct = 0

	for n in range(5,limit):
		
		n = decaN(n)
		check = tree_check(Tree,n)
		if check:
			if check==target: ct += 1
			continue
		chain_tree,chain,pos = [None]*8,[],0

		while True:
			tree_add(chain_tree,n,pos)
			chain += [n]
			n = next_deca(n)
			pos += 1
			loop_start = tree_check(chain_tree,n)
			if loop_start: # already present in chain
				loop_size = pos-loop_start
				for c in chain:
					c_pos = tree_check(chain_tree,c)
					if c_pos>=loop_start: size = loop_size
					else: size = loop_size + loop_start - c_pos
					tree_add(Tree,c,size)
					if size==target: ct += 1
				break
	return ct

# sixties = euler74(1000000,60)
# print(sixties)


# D = {}
# for n in range(1000000):
# 	d = decaN(n)
# 	if d in D:
# 		continue
# 	else : 
# 		nx = next_deca(n)
# 		D[d] = nx

# import euler
# import psyco
# psyco.full()

chains = {}

lookUp = [1] * 10
for x in range(2, 10):
    lookUp[x] = factorial(x)

def chain(x):
    seen = set()
    f = x
    chainSize = 0

    while f not in seen:
        if f in chains:
            chainSize += chains[f]
            break
        seen.add(f)
        chainSize += 1
        strf = str(f)
        f = 0
        for c in list(strf):
            f += lookUp[int(c)]

    chains[x] = chainSize
    return chainSize


count = 0
for x in range(1, 1000001):
    if chain(x) == 60:
        count += 1

print(count)