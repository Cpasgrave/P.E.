"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fib(n):
	f1,f2 = 0,1
	s = 0
	while f2<n:
		f1,f2 = f2,f1+f2
		if f1%2==0: s += f1
	return s



cases = [
10,  # 10
100, # 44
4*10**16,
]

for case in cases:
	print(fib(case))