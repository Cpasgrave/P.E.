"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
"""
def collatz(n):
    c = 1
    while n!=1:
        if n%2 is 0: n //= 2
        else: n = 3*n + 1
        c+=1
    return c

mc = (1,0)
for n in range(1,10**6):
    mc = max(mc,(collatz(n),n))
print(mc[1])
"""

"""
C = {1:1}
for n in range(2,1000000):
	chain=[n]
	while True:
		if n in C:
			for j,c in enumerate(chain):
				C[c]=C[n]+j
			break
		n = n%2 and 3*n+1 or n//2
		chain = [n]+chain
print(max(C,key=C.get))
"""
"""
C = {1:0}
memLimit = 320000
for n in range(2,memLimit):
    chain = [n]
    while 1:
        if not n in C:
            if n&1: n = n+n+n+1
            else: n = n>>1
            chain.append(n)
            continue
        else:
        	for j in range(len(chain)):
        		cc = C[n]+j
        		C[chain.pop()] = cc
        	break
M,L = max(C.items(),key=lambda x:x[1])
for N in range(memLimit,1000000):
    n = N
    m = 0
    while 1:
        if n in C:
            m += C[n]
            if m > L: L,M = m,N
            break
        else:
            if n&1: n = n+n+n+1
            else: n = n>>1
            m += 1

print(M,L)
"""

# Created by Flandre Scarlet


"""
chain = [1,0]
uplimit = 10**6

def request(self, target, add):
    # print("request:",self,target,add)
    global chain
    if target>=len(chain):
        chain += [None]*(target-len(chain))
        chain.append([(self, add)])
    elif chain[target] is None:
        chain[target] = [(self, add)]
    else:
        chain[target] += [(self, add)]

def set(stp, req):
    # req = [*(self, add)]
    # print("set",stp,"to",req)
    global chain
    for r in req:
        rstp = stp + r[1]
        if chain[r[0]] is not None:
            for rr in chain[r[0]]:
                rrstp = rstp + rr[1]
                if type(chain[rr[0]]) is list:
                    set(rrstp, chain[rr[0]])
                chain[rr[0]] = rrstp
        chain[r[0]] = rstp

for p in range(2, uplimit+1):
	stp = 1
	self = p
	if p&1: p = p*3+1
	else: p = p>>1
	while p>uplimit:
		stp += 1
		if p&1: p = p*3+1
		else: p = p>>1
	if p<self and type(chain[p]) is int:
		stp += chain[p]
		if self == len(chain):
			chain.append(stp)
		else:
			if chain[self] is not None:
				set(stp, chain[self])
			chain[self] = stp
	else:
		request(self, p, stp)

maxn = max(chain)
maxi = chain.index(maxn)

print(maxi, ":", maxn)

# print(*map(lambda a: (a[0]+maxi-50,a[1]), enumerate(chain[maxi-50:maxi+50])), sep="\n")

"""
"""
roof = 1200000
cacheMax = 1400000
cache = [0 for _ in range(cacheMax+1)]

cache[2]=1

for n in range(3,roof):
  current = n
  steps = 0
  while 1:
    steps += 1
    if n&1: n = n*3+1
    else: n = n>>1
    if n>cacheMax: continue
    test = cache[n]
    if test:
      cache[current] = test+steps
      break

mx = max(cache)
target = cache.index(mx)
print(mx, target)

"""

"""
uplimit = 5000000
chain = [1,0] + [None]*(uplimit-1)

def expand(n):
    # used when already has a number
    global chain
    if n*2<=uplimit and chain[n*2] is None:
        chain[n*2] = chain[n]+1
        #print("   ", n*2, chain[n*2])
        #print("        expanding:", n*2)
        expand(n*2)
    
    # this may get larger iterations, so not using it
    #if n%3==1 and chain[n//3] is None:
    #    chain[n//3] = chain[n]+1
    #    print("   ", n//3, chain[n//3])
    #    print("        expanding:", n//3)
    #    expand(n//3)
    #print("            end expand:", n)


def search(n):
    # used when chain[n] is None
    global chain
    c = 1
    m = n*3+1 if n&1 else n//2
    while m>uplimit:
        #print("searching...", m)
        c += 1
        m = m*3+1 if m&1 else m//2
    #print("        ask:", m, flush=True)
    if chain[m] is None:
        chain[m] = search(m)
        #print("   ", m, chain[m])
    return chain[m]+c



for p in range(2, uplimit+1):
    if chain[p] is None:
        #print("        need help:", p)
        chain[p] = search(p)
        #print(p, chain[p], flush=True)
    #print("        expanding:", p)
    expand(p)


maxi = max(chain)
maxn = chain.index(maxi)
print(maxn, ":", maxi)
"""


"""
def PE(lim = 10**6):
    d={}; a=0; b=0;
    d=[0]*(lim+1)
    d[1]=1
    def rec(n):
        if n==1: return 1
        if n<=lim:
            if d[n]>0:
                return d[n]
        ans = 1 + rec(n//2) if n%2==0 else 1 + rec(3*n+1)
        if n<=lim: d[n]=ans
        return ans
    
    for n in range(1,lim):
        if rec(n)>b: b=rec(n);a=n
    return a
print(PE(2000000))
"""


# hackerrank solution

def track(i):
    if i>=cache_size:
        if i%2: return track((3*i+1)//2)+2
        else: return track(i//2)+1
    if cache[i]: return cache[i]
    else: 
        if i%2:
            t = track((3*i+1)//2)+2
            cache[i] = t
            return t
        else:
            t = track(i//2)+1
            cache[i] = t
            return t

cases = [10,15,20,5000000]
top = max(cases)
cache_size = top
cache = [1,0,1]+[0 for _ in range(cache_size)]


longest = []
mx = 0
mx_i = 0
for i in range(top+1):
    ti = track(i)
    if i<25: print(i,ti)
    if ti<mx: longest.append(mx_i)
    else:
        mx,mx_i = ti,i
        longest.append(i)

for case in cases:
    lc = longest[case]
    print(lc)

