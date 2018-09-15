
import sys


def first_fib_digits(n_digits = 1000):

	F_n1 = 1
	F_n2 = 1
	i = 2
	while len(str(F_n2)) < int(n_digits):
		c = F_n2
		F_n2 += F_n1
		F_n1 = c
		i += 1


	return i, F_n2







if __name__ == '__main__':
	print(first_fib_digits(sys.argv[1]))