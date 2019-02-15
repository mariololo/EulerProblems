"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

-------
Because we want to check all numbers under a million let us first cache all primes under a million

I think it´s much faster if I look for rotations in the list of primes, instead of on all primes!
"""

from math import sqrt
def is_prime(a):
	if a == 1:
		return False 
	elif a == 2 or a == 3:
		return True
	elif a % 2 == 0 or a % 3 == 0:
		return False
	else:
		for div in range(5, int(sqrt(a))+1, 2):
			if a % div == 0:
				return False
	return True

def primes_under_n(n = 1000000):

	primes = []
	for i in range(1, n):
		if is_prime(i):
			primes.append(i)

	return primes

def rotated_numbers(a):
	a_str = str(a)
	rot_numbers = []
	for i in range(0, len(a_str)):
		rot_numbers.append(int(a_str[i:] + a_str[:i]))
	return rot_numbers

def is_circular_prime(a, primes_to_use):
	for rotated in rotated_numbers(a):
		if rotated not in primes_to_use:
			return False
	return True

def answer(n = 1000000):
	primes_under_million = primes_under_n(n)
	count = 0
	for possible_circular in primes_under_million:
		if is_circular_prime(possible_circular, primes_under_million):
			count += 1
	return count

if __name__ == "__main__":
	#import sys
	print(answer())
