#!/usr/bin/env python3.9

from person import Person
from numba import jit
from time import perf_counter as pc
from time import sleep as pause
import matplotlib as plt



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

def time(n,func):
	times = []
	for i in n:
		start = pc()
		func(i)
		end = pc()
		times.append(end-start)
	return times


def main():
	
	nlist = [i for i in range(30,45)]
	f = Person(20)

	py_times = []
	num_times = []
	cpp_times = []

	print('Starting fib_py')
	py_times = time(nlist, fib_py)
	print('Done')

	print('Starting fib_numba')
	num_times = time(nlist, fib_numba)
	print('Done')

	print('Starting fib_cpp')
	cpp_times = time(nlist, f.fib)
	print('Done')

	plt.plot(nlist,py_times)
	plt.plot(nlist,num_times)
	plt.plot(nlist,cpp_times)
	plt.legend(['fib_py','fib_numba','fib_cpp'])
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.savefig('Times')










if __name__ == '__main__':
	main()
