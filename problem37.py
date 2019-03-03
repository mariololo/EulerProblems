"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 

Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def truncate_right(a):
	a_str = str(a)
	return int(a_str[:-1])

def truncate_left(a):
	a_str = str(a)
	return int(a_str[1:])

def are_truncates_prime(n):
	len_n = len(str(n))
	
	n_right = n
	n_left = n
	for i in range(len_n - 1):
		n_right = truncate_right(n_right)
		n_left = truncate_left(n_left)
		#print("n_right is {}".format(n_right))
		#print("n_left is {}".format(n_left))
		if not is_prime(n_right) or not is_prime(n_left):
			return False

	return True

def loop():
	n = 0
	num = 13
	lst = []
	while n < 11:
		if is_prime(num):
			if are_truncates_prime(num):
				lst.append(num)
				n += 1 
		num += 2
	return lst	

import sys
if __name__ == '__main__':
	print(sum(loop()))
