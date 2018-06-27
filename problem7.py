"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def is_prime(a):

	if a == 1:
		return False
	if a == 2:
		return True
	elif a % 2 == 0:
		return False
	
	i = 3
	sqrt_a =  math.sqrt(a)

	while i <= sqrt_a:
		if a % i == 0:
			return False
		i += 2

	return True

def find_nth_prime(n):
	
	start = 1
	j = 0
	while True:
		if is_prime(start):
			j+=1
			
		if j == n:
			return start

		start += 1


	

if __name__ == '__main__':
	print(find_nth_prime(10001))