"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


import math


def find_pithagorean_triplet(n = 1000):
	for b in range(1, n):
		for a in range(1, b):
			c = n - a - b

			if a**2 + b**2 == c**2:
				return [a, b, c, a*b*c]
	return "no triplet"
	

if __name__	== '__main__':
	print(find_pithagorean_triplet(1000))		
				


