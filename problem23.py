

def sum_proper_divisors(n):

	sum = 0

	for i in range(1,n):
		if n % i == 0:
			sum += i

	return sum

def is_abundant(n):
	"""
	returns -1 if the number is deficient, 0 if it's perfect and 1 if abundant
	"""
	sum_propers = sum_proper_divisors(n)

	if sum_propers > n:
		return True
	else:
		return False

def find_abundant(bound = 28123):

	lst = []

	for i in range(1,bound):
		if is_abundant(i):
			lst.append(i)

	return lst

def integers_not_sum(bound = 28123):

	abundants = find_abundant(bound)

	numbers_not_sum = [i for i in range(1,bound+1)]
	#print("Length of numbers_not_sum is ", len(numbers_not_sum))

	for i in abundants:
		for j in abundants:
			#print("i = ", i,", j = ",j,"...so i+j = ",i+j)
			if i + j <= bound:
				numbers_not_sum[i + j - 1] = 0
				

	return sum(numbers_not_sum)




def main():
	print(integers_not_sum())







if __name__ == '__main__':

	main()