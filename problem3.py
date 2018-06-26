"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def trial_division(n):
	primes = []

	while n % 2 == 0:
		primes.append(2)
		n /= 2

	try_div = 3

	while try_div * try_div <= n:
		if n % try_div == 0:
			primes.append(try_div)
			n /= try_div
		else:
			try_div += 2

	if n!= 1:
		primes.append(int(n))
	return primes







if __name__ == '__main__':
	print(trial_division(600851475143))