def is_palindrom(x):
	return x == x[::-1]

def to_binary(num_base_10):
	return str(bin(num_base_10))[2:]

def loop(limit = 1000000):
	lst = []
	for i in range(limit):
		if is_palindrom(str(i)) and is_palindrom(to_binary(i)):
			lst.append(i)		
	return sum(lst)

if __name__ == '__main__':
	print(loop())
