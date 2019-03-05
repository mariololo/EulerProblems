"""
If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

-------

For a given p and a right triangle, we have two equations to satisfy

p = a + b +c
a^2 = b^2 + c^2

Solving:

p^2 - 2p(c+b) + 2bc = 0

"""
from math import sqrt


def find_b(p,c):
	b_c_values = []
	for b in range(1,p):
		if p**2 == 2 * (c * p - b * c + b * p):
			b_c_values.append((b,c))	

	return b_c_values	

def find_a(p, b, c):
	return p - b- c

import sys
def loop(limit_p = 1000):
	max_p = -1
	max_solutions = -1
	for p in range(5, limit_p):
		sys.stdout.write("Evaluating p = {} \r".format(p))
		sys.stdout.flush()
		count = 0
		for c in range(1,p):
			count += len(find_b(p , c))
		if count > max_solutions:
			max_p = p
			max_solutions = count
			
	return max_p

if __name__ == '__main__':
	print(loop())

