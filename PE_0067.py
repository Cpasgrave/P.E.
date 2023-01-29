'''
Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving
to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'), a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem,
as there are 2**99 altogether! If you could check one trillion (1012)
routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
'''
path = 'H:\\________Boulots\\Python\\Challenge\\Challenges\\Project Euler\\E67.txt'

with open(path, 'r') as f:
    E67 = f.read()

E67 = [[*map(int,E.split())] for E in E67.split('\n')][:-1]

for r,row in enumerate(E67[1:],1):
    lr = len(row)
    for c in range(lr):
        E67[r][c]+=max(E67[r-1][c-1 if c else 0:c+1 if c<lr else c])
print(max(E67[-1])) # 7273


#
