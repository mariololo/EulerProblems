



"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

------------

Because the fraction is less than one in value we have that 

n/m < 1 so n < m

Also both numerator and denominator are two digits so

9 < n,m < 100 with n and m integers

* If we test all numbers we have to test for each n, m = (n-1) numbers, so n*(n-1)! numbers , thats already computationally expensive without taking 
into account computing factors

Let us decompose:
n = 10n_1 + n_2
m = 10m_1 + m_2

where n_1, n_2, m_1, m_2 are positive integers of one digit

Because we are not looking for trivial examples, we disregard when n_2 = m_2 = 0.

The condition to be a curious fraction is that either:

n_1 = m_1 and then n/m = n_2 / m_2
n_1 = m_2 and then n/m = n_2 / m_1
n_2 = m_1 and then n/m = n_1 / m_2
n_2 = m_2 and then n/m = n_1 / m_1


"""
import pandas


def split_tens(n):
	return n // 10, n % 10

def is_curious_fraction(n,m):
	n_1, n_2 = split_tens(n)
	m_1, m_2 = split_tens(m)

	
	if (n_2 != 0 and m_2 != 0):
		if (n_1 == m_1 and n/m == n_2 / m_2):
			return True
		elif (n_1 == m_2 and n/m == n_2 / m_1):
			return True
		elif (n_2 == m_2 and n/m == n_1 / m_1):
                	return True
		elif (n_2 == m_1 and n/m == n_1 / m_2):
                	return True
		else:
			return False
	else:
		return False

def loop_numbers():
	
	fractions = []
	
	for m in range(11,100):
		for n in range(10, m):
			if is_curious_fraction(n, m):
				fractions.append([n,m])			
	
	return fractions

def gcd(n, m):
	while m:
		n, m = m, n % m
	return n
	
	
def reduce_fraction(n,m):
	"""Idea from https://codereview.stackexchange.com/questions/66450/simplify-a-fraction"""
	common_divisor = gcd(n, m)
	
	return n // common_divisor, m // common_divisor
			
def answer():
	"""If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""
		
	fractions = loop_numbers()
	nums = 1
	dens = 1
	for fraction in fractions:
		nums = nums * fraction[0]
		dens = dens * fraction[1] 

	print(fractions)
	print(nums)
	print(dens)	
	_, ans = reduce_fraction(nums, dens)	
	return ans
	
if __name__ == '__main__':
	#import sys
	#print(gcd(int(sys.argv[1]),int(sys.argv[2])))
	#print(reduce_fraction(int(sys.argv[1]),int(sys.argv[2])))

	print(answer())











