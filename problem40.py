"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def champernownse_constant(n_digits = 2000000):
	constant = "0"
	for i in range(1,n_digits):
		constant += str(i)

	return constant

def find_n_digit(n, constant):
	return constant[n]

def solve():
	solution = 1
	constant = champernownse_constant()
	for power in range(0,7):
		digit = int(find_n_digit(10**power, constant))
		print("the 10**{power} digit is {digit}".format(power = power, digit = digit))
		solution *= digit
	return solution

import sys	
if __name__ == '__main__':
	#print(find_n_digit(int(sys.argv[1]), champernownse_constant()))
	print(solve())
