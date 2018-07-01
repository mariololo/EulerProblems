"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""





import sys


def sumdigits(n):
	n_str = str(n)

	ans = 0
	for i in range(len(n_str)):
		ans += int(n_str[i])

	return ans




def main():

	print(sumdigits(int(sys.argv[1]) ** int(sys.argv[2])))






if __name__ == "__main__":
    main()