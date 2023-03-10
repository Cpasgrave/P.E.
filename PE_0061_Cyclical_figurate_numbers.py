'''
Cyclical figurate numbers

Triangle, square, pentagonal, hexagonal, heptagonal,
and octagonal numbers are all figurate (polygonal)
numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281,
has three interesting properties.

The set is cyclic, in that the last two digits of each number
is the first two digits of the next number
(including the last number with the first).
Each polygonal type: triangle (P3,127=8128),
square (P4,91=8281), and pentagonal (P5,44=2882),
is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic
4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
is represented by a different number in the set.
'''
from itertools import count,takewhile,permutations as permu
from collections import defaultdict as dd
from time import perf_counter as time

t = time()

func = {
3:lambda n:n*(n+1)//2,
4:lambda n:n*n,
5:lambda n:n*(3*n-1)//2,
6:lambda n:n*(2*n-1),
7:lambda n:n*(5*n-3)//2,
8:lambda n:n*(3*n-2)
}

def vertices():
    # using each function from the func dict,
    # produces all the vertices, i.e. the 4-digits numbers poduced
    # by the function, keeping info of which func produced it.
    # ex: func triangle num 4523 -> ('45',3,'23')
    vertices = set()
    for fig in range(3,9):
        fourDig = [*takewhile(lambda x:len(str(x))==4,(str(func[fig](c)) for c in count(next(filter(lambda x:len(str(func[fig](x)))==4,count())))))]
        for f in fourDig: vertices.add((f[:2],fig,f[2:]))
    return vertices

def graph(vertices,figOrder):
    # turning the current permutation into a dictionary
    figOrder = {figOrder[i-1]:figOrder[i] for i in range(6)}
    graph = dd(set)
    for v in vertices:
        for v2 in vertices:
            if v[-1]==v2[0]:
                if figOrder[v[1]]==v2[1]:
                    graph[v].add(v2)
    return graph

def find(G,v):
    paths = [[v]]
    new = []
    for i in range(6):
        for path in paths:
            figs = {v[1] for v in path}
            for v2 in [v for v in G[path[-1]]if v[1]not in figs]:
                new.append(path+[v2])
        paths = new
    for path in paths:
        if len(path)==6:
            return path

figOrders = permu(range(3,9),6)
verts = vertices()
nv = len(verts)

sol = []
while True:
    figOrder = next(figOrders,0)
    if figOrder:
        G = graph(verts,figOrder)
        for v in list(G.keys()):
            f = find(G,v)
            if f and f not in sol:
                sol.append(f)
                if f[0][0]==f[-1][-1]:
                    print(f)
                    print(sum([int(v[0]+v[2]) for v in f])) # 28684
                    print((time()-t))
                    exit()

    else: print('Not found'); break
