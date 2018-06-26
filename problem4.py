"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



def largest_palindrome(digits = 3):

	largest = float('-inf')

	for num1 in range(10 ** (digits - 1), 10 ** (digits)):
		for num2 in range(10 ** (digits - 1), 10 ** (digits)):

			prod = num1 * num2

			if (str(prod) == str(prod)[::-1]) and (prod > largest):
				largest = prod

	return largest

if __name__ == '__main__':
	print(largest_palindrome(3))
