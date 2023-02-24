"""
Cuboid route

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, 
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. 
This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""

def PE86(target):
    # naive solution, works for 2000    
    ct = 0
    x = 0
    while ct < target:
        x += 1
        for y in range(1,x+1):
            for z in range(1,y+1):
                a,b = x,y+z # toujours la plus courte des 3 solutions (x>y>z => x et (y+z) vont donner la forme la plus proche du carré
                c = (a**2+b**2)**.5
                if c.is_integer(): ct += 1
    print(ct)
    return x

r = PE86(2000)
print(r)



def PE86(target):

    # x,y,z les cotés du cuboide
    # a,b,c les cotés du triangle rectangle

    # precalcul des carrés, sur une plage estimée, à corriger au besoin...
    squared = {}
    squares = {}
    for n in range(1,10_000):
        sq = n*n
        squares[n] = sq
        squared[sq] = n

    a = 0 # a est aussi M, la limite max pour x,y et z
    ct = 0 # le nombre de solutions rencontrées

    while ct<target:
        a += 1 # on fait progresser a, donc M
        for b in range(1,2*a+1): # b peut valoir jusqu'à 2M
            a2b2 = squares[a]+squares[b]
            if a2b2 in squared:
                # pas besoin de calculer c
                for y in range(1,b//2+1):
                    # pour éviter les doublons, y peut aller jusqu'à b//2
                    # et pour vérifier que M n'est pas dépassé par aucun des x,y,z
                    # comme z = b-y, il ne faut pas que z dépasse a
                    ct += b-y<=a
    return a

r = PE86(2000)
print(r)

from time import perf_counter as tm

t = tm()
r = PE86(1_000_000)
print(r)
print(tm()-t)
