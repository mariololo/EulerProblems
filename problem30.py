"""
Surprisingly there are only three numbers that can
 be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""



from time import time
import sys


def sum_of_power(power = 4):

	lst = []


	for number in range(2,10**(power+1) ):
	#for number in range(1600, 1700):

		digits = []
		#print("number: " + str(number))

		str_number = str(number)

		digits = [int(str_number[j]) ** power for j in range(len(str_number))]


		if sum(digits) == number:
			lst.append(number)


	return lst




if __name__ == '__main__':

	start_time = time()

	list_digits = sum_of_power(int(sys.argv[1]))
	print(list_digits)

	print("sum of numbers is " + str(sum(list_digits)))


	print("Computation took " + str(time() - start_time) +  " s")



