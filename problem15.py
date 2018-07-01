"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

def factorial(n):
	if n < 1:
		return 1
	else:
		return n * factorial(n-1)


def binomial(m,n):
	return factorial(m)/(factorial(m-n) * factorial(n))

def lattice_path(side):
	return int(binomial(side * 2, side))




if __name__ == '__main__':
	print(lattice_path(20))