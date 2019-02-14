"""
Problem 34

-------


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


I think is reasonable to look only up to 1 million. WHY? Well I'm just trying a first number here tbh

Let us also store the result of n! from n = 0 to n = 9 to prevent for repeting computations

Actually I could have done it faster just saving each intermediate step when 
compute factorial(n) but it's only 10 numbers so doesn't matter to much
"""


def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

def compute_n_factorials(max = 10):
	factorials = []
	for i in range(0,max):
		factorials.append(factorial(i))

	return factorials		

def obtain_digits(a):
	n_digits = len(str(a))
	digits = []
	for i in range(n_digits-1, -1, -1):
                digits.append(a // 10**i)
                a = a % 10**i
	return digits

def is_curious_number(a, list_factorials):
	digits = obtain_digits(a)
	digits_factorials = [list_factorials[digit] for digit in digits]
	
	if a == sum(digits_factorials):
		return True

def loop_for_curious(start = 3, end = 700):
	list_factorials = compute_n_factorials()

	curious_numbers = []
	for possible_curious in range(start, end):
		if is_curious_number(possible_curious, list_factorials):
			 curious_numbers.append(possible_curious)

	return curious_numbers

def answer():
	return sum(loop_for_curious(3, 1000000))
	


if __name__ == "__main__":
	import time
	start = time.time()
	print(answer())
	print("Time elapsed: ", time.time() - start) 
