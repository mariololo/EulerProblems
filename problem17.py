"""
If the numbers 1 to 5 are written out in words:
 one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000
 (one thousand) inclusive were written out in words, how many letters would be used?
"""


ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", 'eight', 'nine', 'ten', "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
"seventeen", "eighteen", "nineteen" ]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]




def number2letters(number):
	if 0 <= number < 20:
		return ONES[number]
	elif 20 <= number < 100:
		if number % 10 == 0:
			return TENS[number // 10]
		else:
			return TENS[number // 10] + ONES[number % 10]
	elif 100 <= number < 1000:
		if number == 100:
			return "onehundred"
		if number % 100 == 0:
			return ONES[number // 100] + "hundred"
		else:
			return ONES[number // 100] + "hundred" + "and" + number2letters(number % 100)
	else:
		return "onethousand"


def main():

	ans = 0

	for num in range(1,1001):
		numlet = number2letters(num)

		print(numlet)
		ans += len(numlet)

	print(ans)

if __name__ == "__main__":
	
	main()