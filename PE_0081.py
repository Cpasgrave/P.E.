"""
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving 
right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""


with open("PE_0081.txt",'r') as f:
	matrix = [[*map(int,line.split(','))] for line in f.read().split('\n') if line]


def PE81(matrix):

	l = len(matrix)
	inf = float("inf")

	for s in range(1,2*l-1):
		for i in range(min(s+1,l)):
			j = s-i
			if j<l:
				a = matrix[i-1][j] if i else inf
				b = matrix[i][j-1] if j else inf
				matrix[i][j] += min(a,b)
	print(matrix[-1][-1])


# matrix = [
# [0,1,2,1],
# [3,4,1,4],
# [2,1,8,9],
# [4,1,5,7]
# ]

# matrix = [
# [131,673,234,103,18],
# [201,96,342,965,150],
# [630,803,746,422,111],
# [537,699,497,121,956],
# [805,732,524,37,331],
# ]

PE81(matrix)
