"""

Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 
is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered,
 which produces 80 primes for the consecutive values 0≤n≤79. 
 The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b,
 for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
 starting with n=0.

"""

import math
from itertools import count, islice
import time



def isPrime(a):

	if a <= 1:
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



def list_Primes(limit = 1000):

	lst = []

	for i in range(limit):
		if isPrime(i):
			lst.append(i)

	return lst


def coeffMaxPrimes(rangea = range(-1000,1000) ,rangeb = range(-1000,1000)):

	max_n_primes = 0
	max_a = -2000
	max_b = -2000



	for a in rangea:
		print("testing a = " + str(a))
		for b in rangeb:
			#print("testing b = " + str(b))
			n = 0
			while isPrime((n**2) + (a * n) + b):
				n += 1
			if n > max_n_primes:
				max_n_primes = n
				max_a = a
				max_b = b

	return max_a,max_b,max_n_primes



if __name__  == "__main__":

	start_time = time.time()
	a,b,n = coeffMaxPrimes(range(-1000,1000), list_Primes(1000))

	print("maximum consecutive primes = " + str(n))
	print("a = " + str(a))
	print("b = " + str(b))
	print("a*b = " + str(a*b))

	print("--- %s seconds ---" % (time.time() - start_time))