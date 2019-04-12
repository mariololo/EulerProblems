"""
We shall say that an n-digit number is pandigital if it makes use of
 all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_pandigital(n):
	digits = []
	for dig in str(n):
		if dig in digits:
			return 0
		else:
			digits.append(int(dig))
	digits = sorted(digits)
	if digits[0] == 1:
		last = 1
		if len(digits) == 1:
			return 1
		for dig in digits[1:]:
			if dig != last + 1:
				return 0
			last = dig
		return len(digits)
	else:
		return 0

from math import sqrt
def is_prime(a):
        if a % 3 == 0:
                return False
        else:
                for div in range(5, int(sqrt(a))+1, 2):
                        if a % div == 0:
                                return False
        return True
	
def largest_pandigital():
	print("Searching largest pandigital prime")
	largest = float("-inf")
	running = 9999999
	while True:
		if is_prime(running) and is_pandigital(running) > 0:
			return running
		running = running - 2
		if running % 10000 == 0:
			print(running)

if __name__ == "__main__":
	print(largest_pandigital())



