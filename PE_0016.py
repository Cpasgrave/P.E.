'''
Power digit sum
Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

n = 2**100000
print(sum(map(int,list(str(n)))))

for i in range(30):
	print(f"{i:2} {2**i:10} {sum(map(int,list(str(2**i)))):3}")
