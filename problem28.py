"""
Starting with the number 1 and moving to the right in a clockwise direction
 a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import sys
import time


def diagonals_spiral(side = 5):

	diagonal_nums = [1]

	start_num = 2

	for i in range(3,side+1,2):

		last_num = (start_num - 1) + 4*(i-1)
		counter = 1
		for j in range(start_num,last_num + 1):
			if counter % (i-1) == 0:
				diagonal_nums.append(j)
			counter += 1
		counter = 1

		start_num = last_num + 1

	return diagonal_nums




if __name__  == "__main__":

	start_time = time.time()

	print(sum(diagonals_spiral(int(sys.argv[1]))))

	print("--- %s seconds ---" % (time.time() - start_time))