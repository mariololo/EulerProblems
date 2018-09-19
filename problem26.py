

"""
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


"""


import sys


def long_recurring_cycle(n):
	"""
	we see when the remainder repeats
	"""
	longest = 0
	d_long = 1 

	for i in range(1, int(n)):
		seen = []
		x = 1
		count = 0

		#print("Computing 1/" + str(i))

		while True:
			remainder = x % i
			if remainder == 0:
				#print("No recurring cycle")
				break
			if remainder in seen:
				if len(seen[seen.index(remainder):]) > longest:
					longest = len(seen[seen.index(remainder):])
					d_long = i

				#print("There was a "+str(len(seen[seen.index(remainder):])) + " digit recurring cycle")
				break

			x = remainder * 10

			count += 1
			seen.append(remainder)

	return longest, d_long


		












if __name__ == '__main__':
	print("Mumber with longest recurring cycle is " + str(long_recurring_cycle(sys.argv[1])[1]))