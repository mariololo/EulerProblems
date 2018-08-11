"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


def file2list(file_name):

	file = open(file_name, "r")

	names_raw = file.read()

	names = ""

	for character in names_raw:
		if character != '"':
			names += character

	names = names.split(",")

	return names


def main():


	names = file2list("p022_names.txt")
	ordered_names = sorted(names)


	i = 1

	total_sum = 0

	for name in ordered_names:
		score_name = 0

		for letter in name:

			value_letter = ord(letter) - 64

			score_name += value_letter


		total_sum += score_name * i

		i += 1


	print(total_sum)


if __name__ == '__main__':
	main()