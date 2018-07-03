"""

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""



def factorial(n):
	return 1 if n < 2 else n*factorial(n-1)

def sum_digits(n):
	n_str = str(n)

	ans = 0
	for digit in n_str:
		ans += int(digit)

	return ans




if __name__ == '__main__':

	print(sum_digits(factorial(100)))