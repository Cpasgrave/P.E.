from math import factorial

rg10 = range(10)
rg9 = range(9)
fac = [factorial(n) for n in rg10]

def tree_add(tree,decaN,size):
	node = tree
	for i in rg9:
		value = decaN[i]
		if not node[value]: node[value] = [None,None,None,None,None,None,None,None]
		node = node[value]
	value = decaN[9]
	node[value] = size

def tree_check(tree,decaN):
	node = tree
	for i in rg10:
		value = decaN[i]
		if node[value]==None: return None
		node = node[value]
	return node

def decaN(n):
	D = [0]*10
	while n:
		n,m = divmod(n,10)
		D[m] += 1
	return D

def next_deca(d):
	s = 0
	for i in rg10:
		s += d[i]*fac[i]
	return decaN(s)

def euler74(limit,target):

	Tree = [None]*8

	ct = 0

	for n in range(5,limit):
		
		# print(n)
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

sixties = euler74(1000000,60)
print(sixties)
