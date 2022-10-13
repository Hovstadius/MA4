#!/usr/bin/env python3.9

from person import Person
from numba import jit


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@jit
def fib_numba(n):
	a, b = 0, 1
	while(n-1):
		c = a + b
		a, b = b, c
		n = n - 1
	return c	


def main():
	f = Person(5)
	print(f.get())
	f.set(10)
	print(f.get())
	print(f.fib())
	print(fib_numba(10))
	print(fib_py(10))

if __name__ == '__main__':
	main()
