"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


def sum_primes_below(n):
	ans = 0

	for i in range(2, n, 1):
		if is_prime(i):
			ans += i

	return ans

if __name__ == '__main__':
	print(sum_primes_below(2000000))