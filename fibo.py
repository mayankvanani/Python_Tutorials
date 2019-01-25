## fibonacci numbers module

def fib(n):   ## write fibonacci series upto n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

def fib2(n):   ## reutns fibonacci series upto n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result




if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))

## run this from the terminal

## $ python fibo.py 50

## output we get is ----

## 0 1 1 2 3 5 8 13 21 34
