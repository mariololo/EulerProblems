"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from fractions import gcd


def lcm(start = 1, end = 10):
	number = start

	for i in range(start, end + 1):

		number *= i // gcd(i, number)
	return number
	


		



if __name__ == '__main__':
	print(lcm(1, 20))