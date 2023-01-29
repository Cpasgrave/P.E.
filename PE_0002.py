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