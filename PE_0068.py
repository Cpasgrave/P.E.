"""
Magic 5-gon ring
Problem 68

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.


Working clockwise, and starting from the group of three with
the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely. For example,
the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals:
9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
from itertools import combinations as comb, permutations as perm

def nGon(n):
    nums = [*range(1,2*n+1)]
    ngons = []
    for c in [*comb([n for n in nums if n<10],n)]:
        # combination = inside nums
        tot = 2*sum(c)+sum(n for n in nums if n not in c)
        if tot%n!=0: continue # total sum must be dividable in n integers parts
        line = tot // n
        for p in perm(c[1:]):
            p = [c[0]]+[*p]
            ngon = [(p[i-1],p[i])for i in range(n)]
            cut = ngon.index(max(ngon,key=sum))
            ngon = ngon[cut:]+ngon[:cut]
            ngon = [(line-sum(g),)+g for g in ngon]
            test = {e for g in ngon for e in g if e>0}
            if len(test)==2*n:
                ngon = ''.join([''.join(map(str,g))for g in ngon])
                ngons.append(ngon)
    return ngons

n = 5
ng = nGon(n)
ng = max([*filter(lambda x:len(x)==16,ng)])
print(ng) # 6531031914842725








#
