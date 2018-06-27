"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_squares(n):
	ans = 0

	for i in range(1,n+1):
		ans += i**2
	return ans

def square_sum(n):
	ans = 0

	for i in range(1,n+1):
		ans += i
	return ans**2

if __name__ == '__main__':
	print(square_sum(100) - sum_squares(100))