"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

 
Find the minimal path sum from the top left to the bottom right by moving left, right, up, 
and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""


def sorted_insert(arr,value):
	for i in range(len(arr)-1,-1,-1):
		if value<arr[i]:
			arr.insert(i+1,value)
			return arr
	arr.insert(0,value)
	return arr

def PE83(matrix):
	H = len(matrix)
	W = len(matrix[0])
	neighbors = {(i,j):{(i,j) for (i,j) in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=i<H and 0<=j<W} for i in range(H) for j in range(W)}
	matrix = {(i,j):matrix[i][j] for i in range(H) for j in range(W)}
	ways = [(matrix[(0,0)],(0,0),{(0,0)})]
	ct = 0

	while True:
		tot,here,visited = ways.pop()
		print(tot,here,len(visited))
		for neighbor in neighbors[here]:
			if neighbor in visited: continue
			if neighbor == (H-1,W-1): return tot+matrix[neighbor]
			ways = sorted_insert(ways,(tot+matrix[neighbor],neighbor,visited|{neighbor}))
		print(len(ways))


with open("PE_0083.txt",'r') as f:
	matrix = [[*map(int,line.split(','))] for line in f.read().split('\n') if line]

matrix = [
[5, 1 , 1, 20,1, 1,1],
[9, 9 , 1, 20,1,20,1],
[3, 1 , 1, 20,1,20,1],
[2 ,20,20, 20,1,20,1],
[1, 1 , 1,  2,1,30,1]]

# matrix = [
# [131,673,234,103,18],
# [201,96,342,965,150],
# [630,803,746,422,111],
# [537,699,497,121,956],
# [805,732,524,37,331]
# ]

r = PE83(matrix)
print(r)