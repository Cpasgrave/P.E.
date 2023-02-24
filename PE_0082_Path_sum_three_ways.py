"""
Path sum: three ways

https://projecteuler.net/problem=82

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing 
in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

[[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]]
 
Find the minimal path sum from the left column to the right column in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

def PE82(matrix):

	"""
	progressing column by column, for each line, the best lowest-sum path from previous column gives the 
	value for the current cell, and so on...
	"""

	H,W = len(matrix),len(matrix[0])
	for col in range(1,W):
		new_col = [0]*H
		for line in range(H):
			shift = 0
			mini_sum = float('inf')
			while True:
				stop = 1
				if line-shift>=0:
					stop = 0
					s = sum([matrix[l][col] for l in range(line-shift,line+1)]+[matrix[line-shift][col-1]])
					if s<mini_sum: mini_sum = s
				if line+shift<H:
					stop = 0
					s = sum([matrix[l][col] for l in range(line,line+shift+1)]+[matrix[line+shift][col-1]])
					if s<mini_sum: mini_sum = s
				if stop: break
				shift += 1
			new_col[line] = mini_sum
		for line in range(H):
			matrix[line][col] = new_col[line]
	return min([matrix[i][-1] for i in range(H)])

with open("PE_0082.txt",'r') as f:
	matrix = [[*map(int,line.split(','))] for line in f.read().split('\n') if line]

# matrix = [
# [131,673,234,103,18],
# [201,96,342,965,150],
# [630,803,746,422,111],
# [537,699,497,121,956],
# [805,732,524,37,331]
# ]

# matrix = [
# [10,10, 1,  1,1,20],
# [8, 5 , 1, 10,1,20],
# [7, 1 , 1, 10,1,20],
# [11,1 ,10, 10,1,20],
# [1, 1 ,10, 10,1, 1]]

r = PE82(matrix)
print(r)